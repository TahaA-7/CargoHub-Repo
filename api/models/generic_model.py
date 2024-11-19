import json

from models.base import Base
from providers import data_provider

DATA = []


class Generic_Model(Base):
    def get_units_in_other_endpoint(self, endpoint_unit_id, second_endpoint_arg=None):
        result = []
        if self.endpoint_path == "locations":  # get_locations_in_warehouse
            for x in self.data:
                if x["warehouse_id"] == endpoint_unit_id:
                    result.append(x)
            #
        elif self.endpoint_path == "transfers":
            if second_endpoint_arg == "items":  # get_items_in_transfer  <-- returning object instead of list
                for x in self.data:
                    if x["id"] == endpoint_unit_id:
                        return x["items"]
            #
        elif self.endpoint_path == "items":
            if second_endpoint_arg == "item_line":  # get_items_for_item_line
                for x in self.data:
                    if x["item_line"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_arg == "item_group":  # get_items_for_item_group
                for x in self.data:
                    if x["item_group"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_arg == "item_type":  # get_items_for_item_type
                for x in self.data:
                    if x["item_type"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_arg == "suppliers":  # get_items_for_supplier
                for x in self.data:
                    if x["supplier_id"] == endpoint_unit_id:
                        result.append(x)
            #
        elif self.endpoint_path == "orders":
            if second_endpoint_arg == "items":  # get_items_in_order
                for x in self.data:
                    if x["id"] == endpoint_unit_id:
                        return x["items"]
            elif second_endpoint_arg == "shipments":  # get_orders_in_shipment
                result = []
                for x in self.data:
                    if x["shipment_id"] == endpoint_unit_id:
                        result.append(x["id"])
            elif second_endpoint_arg == "clients":  # get_orders_for_client
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
            if second_endpoint_arg == None:  # get_inventories_for_item
                result = []
                for x in self.data:
                    if x["item_id"] == endpoint_unit_id:
                        result.append(x)
            elif second_endpoint_arg == "totals":  # get_inventory_totals_for_item
                result = {
                "total_expected": 0,
                "total_ordered": 0,
                "total_allocated": 0,
                "total_available": 0
                }
                for x in self.data:
                    if x["item_id"] == endpoint_unit_id:
                        result["total_expected"] += x["total_expected"]
                        result["total_ordered"] += x["total_ordered"]
                        result["total_allocated"] += x["total_allocated"]
                        result["total_available"] += x["total_available"]
                    return result
            #
        else:
            return None
        return result

    def update_units_in_other_endpoint(self, endpoint_unit_id, second_endpoint_arg=None, collection=None):
        if self.endpoint_path == "orders" & second_endpoint_arg == "items":  # update_items_in_order
            order = self.get_single(endpoint_unit_id)
            current = order["items"]
            for x in current:
                found = False
                for y in collection:
                    if x["item_id"] == y["item_id"]:
                        found = True
                        break
                if not found:
                    inventories = data_provider.fetch_generic_endpoint_pool().get_units_in_other_endpoint(x["item_id"])
                    min_ordered = 1_000_000_000_000_000_000
                    min_inventory
                    for z in inventories:
                        if z["total_allocated"] > min_ordered:
                            min_ordered = z["total_allocated"]
                            min_inventory = z
                    min_inventory["total_allocated"] -= x["amount"]
                    min_inventory["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                    data_provider.fetch_generic_endpoint_pool().update_single(min_inventory["id"], min_inventory)
            for x in current:
                for y in collection:
                    if x["item_id"] == y["item_id"]:
                        inventories = data_provider.fetch_generic_endpoint_pool().get_units_in_other_endpoint(x["item_id"])
                        min_ordered = 1_000_000_000_000_000_000
                        min_inventory
                        for z in inventories:
                            if z["total_allocated"] < min_ordered:
                                min_ordered = z["total_allocated"]
                                min_inventory = z
                    min_inventory["total_allocated"] += y["amount"] - x["amount"]
                    min_inventory["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                    data_provider.fetch_generic_endpoint_pool().update_single(min_inventory["id"], min_inventory)
            order["items"] = collection
            self.update_single(endpoint_unit_id, order)
        elif self.endpoint_path == "shipments":  # update_orders_in_shipment
            if second_endpoint_arg == "orders":
                packed_orders = self.get_units_in_other_endpoint(endpoint_unit_id)
                for x in packed_orders:
                    if x not in collection:
                        order = self.get_single(x)
                        order["shipment_id"] = -1
                        order["order_status"] = "Scheduled"
                        self.update_single(x, order)
                for x in collection:
                    order = self.get_single(x)
                    order["shipment_id"] = endpoint_unit_id
                    order["order_status"] = "Packed"
                    self.update_single(x, order)
            elif second_endpoint_arg == "items":  # update_items_in_shipment
                shipment = self.get_single(endpoint_unit_id)
                current = shipment["items"]
                for x in current:
                    found = False
                    for y in collection:
                        if x["item_id"] == y["item_id"]:
                            found = True
                            break
                    if not found:
                        inventories = data_provider.fetch_generic_endpoint_pool().get_units_in_other_endpoint(x["item_id"])
                        max_ordered = -1
                        max_inventory
                        for z in inventories:
                            if z["total_ordered"] > max_ordered:
                                max_ordered = z["total_ordered"]
                                max_inventory = z
                        max_inventory["total_ordered"] -= x["amount"]
                        max_inventory["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                        data_provider.fetch_generic_endpoint_pool().update_single(max_inventory["id"], max_inventory)
                for x in current:
                    for y in collection:
                        if x["item_id"] == y["item_id"]:
                            inventories = data_provider.fetch_generic_endpoint_pool().get_units_in_other_endpoint(x["item_id"])
                            max_ordered = -1
                            max_inventory
                            for z in inventories:
                                if z["total_ordered"] > max_ordered:
                                    max_ordered = z["total_ordered"]
                                    max_inventory = z
                            max_inventory["total_ordered"] += y["amount"] - x["amount"]
                            max_inventory["total_expected"] = y["total_on_hand"] + y["total_ordered"]
                            data_provider.fetch_generic_endpoint_pool().update_single(max_inventory["id"], max_inventory)
                shipment["items"] = collection
                self.update_single(endpoint_unit_id, shipment)
