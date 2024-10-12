from models.generic_model import Generic_Model

from models.warehouses import Warehouses
from models.locations import Locations
from models.transfers import Transfers
from models.items import Items
from models.item_lines import ItemLines
from models.item_groups import ItemGroups
from models.item_types import ItemTypes
from models.inventories import Inventories
from models.suppliers import Suppliers
from models.orders import Orders
from models.clients import Clients
from models.shipments import Shipments

DEBUG = False

ROOT_PATH = "./data/"

_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None

model_endpoint_dict = {_warehouses: "warehouses", _locations: "locations", _transfers: "transfers", _items: "items",
                       _item_lines: "item_lines", _item_groups: "item_groups", _item_types: "item_types", _inventories: "inventories",
                       _suppliers: "suppliers", _orders: "orders", _shipments: "shipments", _clients: "clients"}


def init():
    global _warehouses, _locations, _transfers, _items, _item_lines, _item_groups, _item_types, _inventories, _suppliers, _orders, _clients, _shipments, _clients
    for model_key, endpoint_str in model_endpoint_dict.items():
        # The dictionary uses global variables as keys, so update the variables rather than the dictionary keys by using `global()`.
        globals()[model_key] = Generic_Model(ROOT_PATH, endpoint_str, DEBUG)
        # Also update the dictionary values so that the dictionary content and global variables match.
        model_endpoint_dict[model_key] = globals()[model_key]

    # global _warehouses
    # _warehouses = Warehouses(ROOT_PATH, DEBUG) / _warehouses = Warehouses(ROOT_PATH, "warehouses", DEBUG)
    # global _locations
    # _locations = Locations(ROOT_PATH, DEBUG)
    # global _transfers
    # _transfers = Transfers(ROOT_PATH, DEBUG)
    # global _items
    # _items = Items(ROOT_PATH, DEBUG)
    # global _item_lines
    # _item_lines = ItemLines(ROOT_PATH, DEBUG)
    # global _item_groups
    # _item_groups = ItemGroups(ROOT_PATH, DEBUG)
    # global _item_types
    # _item_types = ItemTypes(ROOT_PATH, DEBUG)
    # global _inventories
    # _inventories = Inventories(ROOT_PATH, DEBUG)
    # global _suppliers
    # _suppliers = Suppliers(ROOT_PATH, DEBUG)
    # global _orders
    # _orders = Orders(ROOT_PATH, DEBUG)
    # global _clients
    # _clients = Clients(ROOT_PATH, DEBUG)
    # global _shipments
    # _shipments = Shipments(ROOT_PATH, DEBUG)


def fetch_generic_endpoint_pool(endpoint):
    match endpoint:
        case "warehouses":
            return _warehouses
        case "locations":
            return _locations
        case "items":
            return _items
        case "item_lines":
            return _item_lines
        case "item_groups":
            return _item_groups
        case "item_types":
            return _item_types
        case "inventories":
            return _inventories
        case "suppliers":
            return _suppliers
        case "orders":
            return _orders
        case "clients":
            return _clients
        case "shipments":
            return _shipments
        case _:
            return None


# def fetch_warehouse_pool():
#     return _warehouses


# def fetch_location_pool():
#     return _locations


# def fetch_transfer_pool():
#     return _transfers


# def fetch_item_pool():
#     return _items


# def fetch_item_line_pool():
#     return _item_lines


# def fetch_item_group_pool():
#     return _item_groups


# def fetch_item_type_pool():
#     return _item_types


# def fetch_inventory_pool():
#     return _inventories


# def fetch_supplier_pool():
#     return _suppliers


# def fetch_order_pool():
#     return _orders


# def fetch_client_pool():
#     return _clients


# def fetch_shipment_pool():
#     return _shipments
