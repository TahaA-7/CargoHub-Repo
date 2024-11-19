import socketserver
import http.server
import json

from providers import auth_provider
from providers import data_provider

from processors import notification_processor


class ApiRequestHandler(http.server.BaseHTTPRequestHandler):

    def handle_get_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "get"):
            self.send_response(403)
            self.end_headers()
            return

        paths = len(path)

        if (paths) > 1:
            endpoint_unit_id = int(path[1])
        match paths:
            case 1:
                first_level_endpoint = data_provider.fetch_generic_endpoint_pool(path[0]).get_all()
                self.close_handle_get_method(first_level_endpoint)
            case 2:
                endpoint_unit_id = int(path[1])
                endpoint_unit = data_provider.fetch_generic_endpoint_pool(path[0]).get_single(endpoint_unit_id)
                self.close_handle_get_method(endpoint_unit)
            case 3:
                #contingent upon path[2]
                if path[0] == "warehouses":
                    if path[2] == "locations":
                        endpoint_unit_id = int(path[1])
                        # PATHS 0 and 2 MUST BE SWAPPED SINCE YOU ARE LOOKING FOR WAREHOUSES IN THE LOCATIONS DATABASE (or json)
                        # fetch_location_pool().get_locations_in_warehouse()
                        endpoint_unit = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(endpoint_unit)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "transfers":
                    if path[2] == "items":
                        endpoint_unit_id = int(path[1])
                        # fetch_transfer_pool().get_items_in_transfer
                        endpoint_unit = data_provider.fetch_generic_endpoint_pool(path[0]).get_units_in_endpoint(endpoint_unit_id, path[2])
                        self.close_handle_get_method(endpoint_unit)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "items":
                    if path[2] == "inventory":
                        endpoint_unit_id = int(path[1])
                        # fetch_inventory_pool().get_inventories_for_item()
                        inventories = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(inventories)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "item_lines":
                    if path[2] == "items":
                        # fetch_item_pool().get_items_for_item_line()
                        items = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "item_groups":
                    if path[2] == "items":
                        # fetch_item_pool().get_items_for_item_group()
                        items = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "item_types":
                    if path[2] == "items":
                        # fetch_item_pool().get_items_for_item_type()
                        items = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "suppliers":
                    if path[2] == "items":
                        # fetch_item_pool().get_items_for_supplier()
                        items = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "orders":
                    if path[2] == "items":
                        # fetch_order_pool().get_items_in_order()
                        items = data_provider.fetch_generic_endpoint_pool(path[0]).get_units_in_endpoint(endpoint_unit_id, path[2])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "clients":
                    if path[2] == "orders":
                        # fetch_order_pool().get_orders_for_client()
                        orders = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(orders)
                    else:
                        self.send_response(404)
                        self.end_headers()
                elif path[0] == "shipments":
                    if path[2] == "orders":
                        # fetch_order_pool().get_orders_in_shipment()
                        orders = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                        self.close_handle_get_method(orders)
                    elif path[2] == "clients":
                        # fetch_shipment_pool().get_items_in_shipment()
                        items = data_provider.fetch_generic_endpoint_pool(path[0]).get_units_in_endpoint(endpoint_unit_id, path[2])
                        self.close_handle_get_method(items)
                    else:
                        self.send_response(404)
                        self.end_headers()
                else:
                    self.send_response(404)
                    self.end_headers()
            case 4:
                if path[1] == "inventory" and path[3] == "totals":
                    endpoint_unit_id = int(path[0])
                    # fetch_inventory_pool().get_inventory_totals_for_item()
                    endpoint_unit = data_provider.fetch_generic_endpoint_pool(path[2]).get_units_in_endpoint(endpoint_unit_id, path[0])
                    self.close_handle_get_method(endpoint_unit)
                else:
                    self.send_response(404)
                    self.end_headers()
            case _:
                self.send_response(404)
                self.end_headers()

    def close_handle_get_method(self, single_or_collection):
        self.send_response(200)  # Send this because the user has access to the endpoint. The content is irrelevant at this point.
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(single_or_collection).encode("utf-8"))

    def do_GET(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_get_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_post_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "post"):
            self.send_response(403)
            self.end_headers()
            return
        # try:
        #     content_length = int(self.headers["Content-Length"])
        #     post_data = self.rfile.read(content_length)
        #     new_transfer = json.loads(post_data.decode())
        #     data_provider.fetch_generic_endpoint_pool().add_single(new_transfer)
        #     data_provider.fetch_generic_endpoint_pool().save()
        #     if path[0] == "transfers":
        #         notification_processor.push(f"Scheduled batch transfer {new_transfer['id']}")
        #     self.send_response(201)
        #     self.end_headers
        # except Exception:
        #     self.send_response(404)
        #     self.end_headers()
        if path[0] == "transfers":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            new_transfer = json.loads(post_data.decode())
            data_provider.fetch_generic_endpoint_pool(path[0]).add_single(new_transfer)
            data_provider.fetch_generic_endpoint_pool(path[0]).save()
            notification_processor.push(f"Scheduled batch transfer {new_transfer['id']}")
            self.send_response(201)
            self.end_headers()
        else:
            try:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                new_warehouse = json.loads(post_data.decode())
                data_provider.fetch_generic_endpoint_pool(path[0]).add_single(new_warehouse)
                data_provider.fetch_generic_endpoint_pool(path[0]).save()
                self.send_response(201)
                self.end_headers()
            except Exception:
                self.send_response(404)
                self.end_headers()

    def do_POST(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_post_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_put_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "put"):
            self.send_response(403)
            self.end_headers()
            return
        if path[0] == "transfers":
            paths = len(path)
            match paths:
                case 2:
                    transfer_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_transfer = json.loads(post_data.decode())
                    data_provider.fetch_generic_endpoint_pool(path[0]).update_single(transfer_id, updated_transfer)
                    data_provider.fetch_generic_endpoint_pool(path[0]).save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "commit":
                        transfer_id = int(path[1])
                        transfer = data_provider.fetch_generic_endpoint_pool(path[0]).get_transfer(transfer_id)
                        for x in transfer["items"]:
                            inventories = data_provider.fetch_generic_endpoint_pool("inventories").get_units_in_other_endpoint(x["item_id"])
                            for y in inventories:
                                if y["location_id"] == transfer["transfer_from"]:
                                    y["total_on_hand"] -= x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_generic_endpoint_pool("inventories").update_single(y["id"], y)
                                elif y["location_id"] == transfer["transfer_to"]:
                                    y["total_on_hand"] += x["amount"]
                                    y["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                                    y["total_available"] = y["total_on_hand"] - y["total_allocated"]
                                    data_provider.fetch_generic_endpoint_pool("inventories").update_single(y["id"], y)
                        transfer["transfer_status"] = "Processed"
                        data_provider.fetch_generic_endpoint_pool(path[0]).update_single(transfer_id, transfer)
                        notification_processor.push(f"Processed batch transfer with id:{transfer['id']}")
                        data_provider.fetch_generic_endpoint_pool(path[0]).save()
                        data_provider.fetch_generic_endpoint_pool("inventories").save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "orders":
            paths = len(path)
            match paths:
                case 2:
                    order_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_order = json.loads(post_data.decode())
                    data_provider.fetch_generic_endpoint_pool(path[0]).update_single(order_id, updated_order)
                    data_provider.fetch_generic_endpoint_pool(path[0]).save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "items":
                        order_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_generic_endpoint_pool(path[0]).update_units_in_other_endpoint(order_id, updated_items)
                        data_provider.fetch_generic_endpoint_pool(path[0]).save()
                        self.send_response(200)
                        self.end_headers()
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        elif path[0] == "shipments":
            paths = len(path)
            match paths:
                case 2:
                    shipment_id = int(path[1])
                    content_length = int(self.headers["Content-Length"])
                    post_data = self.rfile.read(content_length)
                    updated_shipment = json.loads(post_data.decode())
                    data_provider.fetch_generic_endpoint_pool(path[0]).update_single(shipment_id, updated_shipment)
                    data_provider.fetch_generic_endpoint_pool(path[0]).save()
                    self.send_response(200)
                    self.end_headers()
                case 3:
                    if path[2] == "orders":
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_orders = json.loads(post_data.decode())
                        data_provider.fetch_generic_endpoint_pool("orders").update_units_in_other_endpoint(shipment_id, updated_orders)
                        data_provider.fetch_generic_endpoint_pool("orders").save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "items":
                        shipment_id = int(path[1])
                        content_length = int(self.headers["Content-Length"])
                        post_data = self.rfile.read(content_length)
                        updated_items = json.loads(post_data.decode())
                        data_provider.fetch_generic_endpoint_pool("shipments").update_units_in_other_endpoint(shipment_id, updated_items)
                        data_provider.fetch_generic_endpoint_pool("shipments").save()
                        self.send_response(200)
                        self.end_headers()
                    elif path[2] == "commit":
                        pass
                    else:
                        self.send_response(404)
                        self.end_headers()
                case _:
                    self.send_response(404)
                    self.end_headers()
        else:
            try:
                single_id = int(path[1])
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                updated_single = json.loads(post_data.decode())
                data_provider.fetch_generic_endpoint_pool(path[0]).update_single(single_id, updated_single)
                data_provider.fetch_generic_endpoint_pool(path[0]).save()
                self.send_response(200)
                self.end_headers()
            except Exception:
                self.send_response(404)
                self.end_headers()

    def do_PUT(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_put_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def handle_delete_version_1(self, path, user):
        if not auth_provider.has_access(user, path, "delete"):
            self.send_response(403)
            self.end_headers()
            return
        try:
            single_id = int(path[1])
            data_provider.fetch_generic_endpoint_pool(path[0]).remove_single(single_id)
            data_provider.fetch_generic_endpoint_pool(path[0]).save()
            self.send_response(200)
            self.end_headers()
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_delete_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()

    def do_REQUEST(self, request_type):
        api_key = self.headers.get("API_KEY")
        user = auth_provider.get_user(api_key)
        if user == None:
            self.send_response(401)
            self.end_headers()
        else:
            try:
                path = self.path.split("/")
                if len(path) > 3 and path[1] == "api" and path[2] == "v1":
                    self.handle_delete_version_1(path[3:], user)
            except Exception:
                self.send_response(500)
                self.end_headers()


if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("", PORT), ApiRequestHandler) as httpd:
        auth_provider.init()
        data_provider.init()
        notification_processor.start()
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
