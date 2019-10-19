from bc4py.config import C
from typing import Optional, Deque
from collections import deque, namedtuple


class Const:
    """const params, do not edit this file"""
    REST_API = 'http://127.0.0.1:3000'
    DATABASE_PATH = 'pool.db'
    HOST_NAME = 'localhost'

    # how to payout? 'transaction' or 'coinbase'
    PAYOUT_METHOD: Optional[str] = None


# accept lower works divided by co_efficiency
co_efficiency = {
    C.BLOCK_YES_POW: 65536,
    C.BLOCK_X16S_POW: 256,
    C.BLOCK_X11_POW: 1,
}

# coinbase distribution payout (option)
Distribution = namedtuple('Distribution', [
    'time', 'algorithm', 'distribution'])
distribution_list: Deque[Distribution] = deque(maxlen=50)


# pool status recode for a day per a minute
PoolStatus = namedtuple('PoolStatus', [
    'time', 'workers', 'pool_hashrate', 'network_hashrate', 'share'])
pool_status_list: Deque[PoolStatus] = deque(maxlen=60*24)  # for 1 day


__all__ = [
    "Const",
    "co_efficiency",
    "Distribution",
    "distribution_list",
    "PoolStatus",
    "pool_status_list",
]
