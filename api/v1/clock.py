from time import time

from api.v1 import api_v1

@api_v1.route('/time/<float:t1>')
def netime_time(t1: float) -> str:
    return str(time())
