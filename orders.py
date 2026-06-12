import logging

def place_order(client, symbol, side, order_type, quantity, price=None):

    logging.info("Sending Order")

    if order_type == "LIMIT":

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    else:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )

    logging.info(f"Order Response: {order}")

    return order