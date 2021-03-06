import os
import sys
import json

from decimal import Decimal

from base_model import BaseAuctionModel

START_PERCENT = -40
FINISH_PERCENT = -10
MARKUP_PERCENT = 15
PAIR = "MDTRUB"

OUR_ADDRESSES = [
    "0xC0CCab7430aEc0C30E76e1dA596263C3bdD82932",
]


if __name__ == '__main__':
    our_addresses = os.environ.get("OUR_ADDRESSES", OUR_ADDRESSES)
    if isinstance(our_addresses, str):
        our_addresses = our_addresses.split()

    pair = os.environ.get("PAIR", PAIR)

    start_percent = Decimal(os.environ.get("START_PERCENT", START_PERCENT))
    finish_percent = Decimal(os.environ.get("FINISH_PERCENT", FINISH_PERCENT))
    markup_percent = Decimal(os.environ.get("MARKUP_PERCENT", MARKUP_PERCENT))

    model = BaseAuctionModel(our_addresses=our_addresses, start_percent=start_percent,
                             finish_percent=finish_percent, markup_percent=markup_percent)

    for line in sys.stdin:
        signal = json.loads(line)

        price = model.calculate_price_for_auction(signal, pair=pair)

        if price:
            stance = {'price': price / 10 ** 18}
            print(json.dumps(stance), flush=True)
