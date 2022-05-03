import time
from web3 import Web3
from web3.middleware import geth_poa_middleware
from arbitrage_paths import get_path_infos
from utils import *


def handle_event(event):
    get_last_price(arb_info)


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            print(len(event_filter.get_new_entries()))
            handle_event(event)
        time.sleep(poll_interval)


def main():

    block_filter = w3.eth.filter('latest')
    log_loop(block_filter, 0.1)


main()
