from datetime import datetime
import json

DATA = []

class Base:
    # def __init__():
    #     pass
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

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"
