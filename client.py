from binance.client import Client

def get_client(api_key, api_secret):
    return Client(
        api_key,
        api_secret,
        testnet=True
    )