from django.http import JsonResponse
from .models import ApiKey


def validate_api_key(view_func):
    def wrapped_view(request, *args, **kwargs):
        api_key = request.headers.get('Authorization')
        if not api_key:
            return JsonResponse({"error": "API key required"}, status=401)

        try:
            key_record = ApiKey.objects.get(key=api_key, is_active=True)
        except ApiKey.DoesNotExist:
            return JsonResponse({"error": "Invalid or inactive API key"}, status=403)

        warehouse_id = kwargs.get('warehouse_id')
        if warehouse_id:
            if not key_record.warehouses.filter(id=warehouse_id).exists():
                return JsonResponse({"error": "Access to this warehouse is not allowed"}, status=403)

        request.client = key_record.client 
        return view_func(request, *args, **kwargs)
    return wrapped_view

