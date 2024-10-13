import json

from models.base import Base

DATA = []


class Generic_Model(Base):
    def __init__(self, root_path, endpoint_path=None, is_debug=False):
        if endpoint_path == None:
            return
        self.endpoint_path = f"{endpoint_path}.json"
        self.data_path = root_path + endpoint_path
        self.load(is_debug)

    def get_first_level_endpoint_all(self):
        return self.data

    def get_endpoint_unit(self, endpoint_unit_id):
        for x in self.data:
            if x["id"] == endpoint_unit_id:
                return x
        return None

    def get_path2_units_in_path1(self, endpoint_unit_id, second_endpoint_type=None):
        result = []
        if self.endpoint_path == "locations":  # get_locations_in_warehouse
            for x in self.data:
                if x["warehouse_id"] == endpoint_unit_id:
                    result.append(x)
            #
        elif self.endpoint_path == "transfers":
            if second_endpoint_type == "items":  # get_items_in_transfer  <-- returning object instead of list
                for x in self.data:
                    if x["id"] == endpoint_unit_id:
                        return x["items"]
            #
        elif self.endpoint_path == "items":
            if second_endpoint_type == "item_line":  # get_items_for_item_line
                for x in self.data:
                    if x["item_line"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_type == "item_group":  # get_items_for_item_group
                for x in self.data:
                    if x["item_group"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_type == "item_type":  # get_items_for_item_type
                for x in self.data:
                    if x["item_type"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_type == "suppliers":  # get_items_for_supplier
                for x in self.data:
                    if x["supplier_id"] == endpoint_unit_id:
                        result.append(x)
            #
        elif self.endpoint_path == "orders":
            if second_endpoint_type == "items":  # get_items_in_order
                for x in self.data:
                    if x["id"] == endpoint_unit_id:
                        return x["items"]
            elif second_endpoint_type == "shipments":  # get_orders_in_shipment
                result = []
                for x in self.data:
                    if x["shipment_id"] == endpoint_unit_id:
                        result.append(x["id"])
            elif second_endpoint_type == "clients":  # get_orders_for_client
                result = []
                for x in self.data:
                    if x["ship_to"] == endpoint_unit_id or x["bill_to"] == endpoint_unit_id:
                        result.append(x)
                return result
            #
        elif self.endpoint_path == "shipments":  # get_items_in_shipment
            for x in self.data:
                if x["id"] == endpoint_unit_id:
                    return x["items"]
            return None
        elif self.endpoint_path == "inventories":
            result = []
            for x in self.data:
                if x["item_id"] == endpoint_unit_id:
                    result.append(x)
            #
        else:
            return None
        return result

    def add_endpoint(self, endpointlv2):
        endpointlv2["created_at"] = self.get_timestamp()
        endpointlv2["updated_at"] = self.get_timestamp()
        self.data.append(endpointlv2)

    def update_endpoint(self, endpointlv2_id, endpointlv2):
        endpointlv2["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == endpointlv2_id:
                self.data[i] = endpointlv2
                break

    def remove_edpoint(self, endpointlv2_id):
        for x in self.data:
            if x["id"] == endpointlv2_id:
                self.data.remove(x)

    def load(self, is_debug):
        if is_debug:
            self.data = DATA
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()

    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
