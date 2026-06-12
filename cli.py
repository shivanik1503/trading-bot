import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

validate_side(args.side)
validate_order_type(args.type)

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_KEY"

client = get_client(
    api_key,
    api_secret
)

order = place_order(
    client,
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

print("Order ID:", order["orderId"])
print("Status:", order["status"])
print("Symbol:", order["symbol"])
print("Side:", order["side"])
print("Type:", order["type"])
print("Order placed successfully!")