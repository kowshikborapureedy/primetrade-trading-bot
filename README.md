# PrimeTrade.ai - Simplified Trading Bot (Binance Futures Testnet)

[cite_start]A robust, production-ready Python command-line utility built to place automated Market and Limit orders on the Binance Futures Demo platform (USDT-M)[cite: 4, 6].

## Project Architecture
[cite_start]The codebase strictly adheres to a decoupled structure separating the core wrapper modules from the runtime operational CLI interface[cite: 30, 49]:
- [cite_start]`bot/client.py`: Configuration wrapper handling secure authentication with the API layer[cite: 53].
- [cite_start]`bot/orders.py`: Core logic routines processing Market and Limit type transactions[cite: 54].
- [cite_start]`bot/validators.py`: Input assertions validating boundaries for quantity and price constraints[cite: 55].
- [cite_start]`bot/logging_config.py`: Non-intrusive stream pipelines writing clean metrics to local tracking files[cite: 31, 56].
- [cite_start]`bot/cli.py`: Unified operational entry engine parsed using the Python argparse library[cite: 19, 57].

## Local Installation Setup
1. Clone this project workspace to your local environment.
2. [cite_start]Ensure you have Python 3.8+ active on your workstation[cite: 15].
3. [cite_start]Run the following command to download core module packages[cite: 38]:
   ```bash
   pip install -r requirements.txt
**   #Usage Execution Examples**
1. Market Order Execution
  python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
  2. Limit Order Execution
  python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000