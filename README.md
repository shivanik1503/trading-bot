# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features

* MARKET Orders
* LIMIT Orders
* BUY and SELL support
* Command Line Interface (CLI)
* Input Validation
* Logging
* Error Handling

## Installation

```bash
pip install -r requirements.txt
```

## Run MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Project Structure

trading_bot/

├── bot/

│   ├── **init**.py

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

├── logs/

│   └── trading.log

├── cli.py

├── requirements.txt

└── README.md

## Logging

Logs are stored in:

logs/trading.log
