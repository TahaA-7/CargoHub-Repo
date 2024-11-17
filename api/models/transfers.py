import json

from models.base import Base

DATA = []


class Transfers(Base):
    def get_items_in_transfer(self, transfer_id):
        for x in self.data:
            if x["id"] == transfer_id:
                return x["items"]
        return None

    def add_single(self, transfer):
        transfer["transfer_status"] = "Scheduled"
        Base.add_single(transfer)
