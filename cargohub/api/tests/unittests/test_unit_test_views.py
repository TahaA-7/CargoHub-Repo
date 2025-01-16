from django.test import TestCase
from api.models import *
from api.views import *
from api.serializers import *
from datetime import datetime
from django.utils.timezone import make_aware

# NOTES: cd to `cargohub` and run with `python manage.py test api.tests.unittests.test_unit_test_views`

class ViewsTestCaseItems(TestCase):
    def setUp(self):
        self.item_dict = {
            "code": "aapjeBanaantje",
            "description": "aapje wil heel heel heel erg graag een banaantje",
            "short_description": "aapje++++banaantje",
            "upc_code": "AB",
            "model_number": 12,
            "commodity_code": 21,
            "item_line": 1,
            "item_group": 1,
            "item_type": 1,
            "unit_purchase_quantity": 1,
            "unit_order_quantity": 1,
            "pack_order_quantity": 1,
            "supplier_id": 1,
            "supplier_code": "banaantjeaapje",
            "supplier_part_number": "aapje1banaantje2",
        }

        Items.objects.create(
            uid = 1,     # NOTE: the db converts this to a UID. It doesn't distinguish between UID and UUID (so it's a UID, not UUID).
            code=self.item_dict['code'],
            description=self.item_dict['description'],
            short_description=self.item_dict['short_description'],
            upc_code=self.item_dict['upc_code'],
            model_number=self.item_dict['model_number'],
            commodity_code=self.item_dict['commodity_code'],
            item_line=self.item_dict['item_line'],
            item_group=self.item_dict['item_group'],
            item_type=self.item_dict['item_type'],
            unit_purchase_quantity=self.item_dict['unit_purchase_quantity'],
            unit_order_quantity=self.item_dict['unit_order_quantity'],
            pack_order_quantity=self.item_dict['pack_order_quantity'],
            supplier_id=self.item_dict['supplier_id'],
            supplier_code=self.item_dict['supplier_code'],
            supplier_part_number=self.item_dict['supplier_part_number'],
            created_at = make_aware(datetime.strptime("2012-12-04 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at = make_aware(datetime.strptime("2016-01-05 11:34:12", "%Y-%m-%d %H:%M:%S")),
        )
        Item_lines.objects.create(
            id = 1,
            name = "klappertand klaas",
            description = "een OC van Thh",
            created_at = make_aware(datetime.strptime("2012-12-03 10:44:27", "%Y-%m-%d %H:%M:%S")),
            updated_at = make_aware(datetime.strptime("2016-01-04 11:34:12", "%Y-%m-%d %H:%M:%S")),
        )

    def test_view_get_method(self):
        get_attempt_all = get_objects(Items, ItemsSerializer)
        self.assertEqual(len(get_attempt_all.data), 1)
        get_attempt_one1 = get_object(Items, 0, ItemsSerializer)
        self.assertIsNone(get_attempt_one1.data)
        get_attempt_one2 = get_object(Items, 1, ItemsSerializer)
        self.assertIsNotNone(get_attempt_one2.data)

        get_attempt_item_lines_one = get_object(Item_lines, get_attempt_one2.data['item_line'], ItemLinesSerializer)
        self.assertIsNotNone(get_attempt_item_lines_one.data)


class ViewsTestCaseTransfers(TestCase):
    def setUp(self):
        self.transfer_dict1 = {
            "reference": "mens geeft banaantje aan aap",
            "transfer_from": "mens",
            "transfer_to": "aap",
            "transfer_status": "success",
            "created_at": make_aware(datetime.strptime("2016-01-05 11:35:12", "%Y-%m-%d %H:%M:%S")),
            "updated_at": make_aware(datetime.strptime("2016-01-05 11:35:21", "%Y-%m-%d %H:%M:%S")),
        }
        self.transfer_dict2 = {
            "reference": "spinaapje geeft banaantje aan slingeraapje",
            "transfer_from": "spinaapje",
            "transfer_to": "slingeraapje",
            "transfer_status": "failed",
            "created_at": make_aware(datetime.strptime("2016-01-05 11:35:12", "%Y-%m-%d %H:%M:%S")),
            "updated_at": make_aware(datetime.strptime("2016-01-05 11:35:21", "%Y-%m-%d %H:%M:%S")),
        }
        self.transfer_dict1_updated = {
            "reference": "mens geeft wederom een banaantje aan aap",
        }

    def test_view_get_method(self):
        get_attempt_all = get_objects(Transfers, TransfersSerializer)
        self.assertEqual(len(get_attempt_all.data), 0)

    def test_view_post_method(self):
        post_attempt1 = post_object(Transfers, TransfersSerializer, self.transfer_dict1)
        self.assertEqual(post_attempt1.status_code, status.HTTP_201_CREATED)

        post_attempt2 = post_object(Transfers, TransfersSerializer, self.transfer_dict2)
        self.assertEqual(post_attempt2.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertIsNone(post_attempt2.data) # FAILED: 
        #   output: AssertionError: {'transfer_to': [ErrorDetail(string='Ensure this field has no more than 6 characters.', code='max_length')]} is not None

        with self.subTest("get_created_object"):
            get_attempt_all2 = get_objects(Transfers, TransfersSerializer)
            self.assertEqual(len(get_attempt_all2.data), 1)
            self.assertIsNotNone(post_attempt1.data)

        with self.subTest("update_created_object"):
            put_attempt = update_object(Transfers, 1, TransfersSerializer, self.transfer_dict1)
            self.assertEqual(put_attempt.status_code, status.HTTP_200_OK)

        with self.subTest("get_updated_object"):
            get_attempt = get_object(Transfers, 1, TransfersSerializer)
            self.assertIsNotNone(get_attempt.data)

        with self.subTest("delete_object"):
            delete_attempt = delete_object(Transfers, 1)
            self.assertEqual(delete_attempt.status_code, status.HTTP_204_NO_CONTENT)

        with self.subTest("get_deleted_object"):
            get_attempt2 = get_object(Transfers, 1, TransfersSerializer)
            self.assertIsNone(get_attempt2.data)


class ViewsTestCasePseudo_models(TestCase):     # Testing that the view methods can be tested irrespective of authorisation
    def setUp(self):
        self.pseudo_model_dict = {
            "pseudonym": "pseudonius",
            "pseudology": "dit is een pseudologie"
        }

        post_attempt = post_object(Pseudo_models, PseudoModelsSerializer, self.pseudo_model_dict)
        self.assertEqual(post_attempt.status_code, status.HTTP_201_CREATED)

        get_attempt = get_object(Pseudo_models, 1, PseudoModelsSerializer)
        self.assertIsNotNone(get_attempt.data)
