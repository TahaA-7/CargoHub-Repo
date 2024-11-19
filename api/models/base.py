from datetime import datetime
import json
import os

DATA = []

class Base:
    # def __init__():
    #     pass
    def __init__(self, root_path, endpoint_path=None, is_debug=False):
        if endpoint_path == None:
            return
        self.endpoint_path = f"{endpoint_path}.json"
        self.data_path = os.path.join(root_path, self.endpoint_path)
        self.load(is_debug)

    def get_all(self):
        return self.data

    def get_single(self, endpoint_unit_id):
        for x in self.data:
            if x["id"] == endpoint_unit_id:
                return x
        return None

    def add_single(self, endpointlv2):
        endpointlv2["created_at"] = self.get_timestamp()
        endpointlv2["updated_at"] = self.get_timestamp()
        self.data.append(endpointlv2)

    def update_single(self, endpointlv2_id, endpointlv2):
        endpointlv2["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == endpointlv2_id:
                self.data[i] = endpointlv2
                break

    def remove_single(self, endpointlv2_id):
        for x in self.data:
            if x["id"] == endpointlv2_id:
                self.data.remove(x)

    def load(self, is_debug):
        if is_debug:
            self.data = DATA
        else:
            try:
                print(f"Loading data from: {self.data_path}")
                with open(self.data_path, "r") as f:
                    self.data = json.load(f)
            except FileNotFoundError:
                print(f"File not found: {self.data_path}")
                self.data = []


    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"
