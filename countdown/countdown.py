from walrus import Walrus
from time import time

from uuid import UUID, uuid4
import struct

class Cache:
    __instance = None

    @staticmethod
    def getInstance():
        if Cache.__instance == None:
            Cache()
        return Cache.__instance

    def __init__(self):
        if Cache.__instance != None:
            raise Exception("Cache is a singleton. Use Cache.getInstance()")
        Cache.__instance = self
        self.db = Walrus(host='localhost', port=6379, db=0)

    def add_countdown(self, total: float) -> UUID:
        countdown_id = uuid4()
        countdown = self.db.Hash(str(countdown_id))
        countdown.update(id=str(countdown_id), start=-1, total=total)
        return self.get_countdown(str(countdown_id))

    def start_countdown(self, id: UUID) -> dict:
        countdown = self.db.Hash(str(id))
        countdown.update(start=time())
        return countdown.as_dict(decode=True)

    def stop_countdown(self, id: UUID) -> dict:
        countdown = self.db.Hash(str(id))
        countdown.update(start=-1)
        return countdown.as_dict(decode=True)

    def reset_countdown(self, id: UUID) -> dict:
        countdown = self.db.Hash(str(id))
        countdown.update(start=time())
        return countdown.as_dict(decode=True)

    def get_countdown(self, id: UUID) -> dict:
        countdown = self.db.Hash(str(id))
        return countdown.as_dict(decode=True)
