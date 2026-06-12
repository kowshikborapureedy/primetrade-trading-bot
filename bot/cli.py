import sys
import argparse
from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.client import get_binance_client
from bot.orders import execute_order

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "market", "limit"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, default=None, help="Price (Required for LIMIT orders)")
    
    args = parser.parse_args()
    
    try:
        # Validate inputs
        symbol, side, order_type, quantity, price = validate_inputs(
            args.symbol, args.side, args.type, args.quantity, args.price
        )
        
        # Connect to client
        client = get_binance_client()
        
        # Execute order
        result = execute_order(client, symbol, side, order_type, quantity, price)
        
        # Print summary output
        print("\n" + "="*40)
        if result["success"]:
            print("🟢 ORDER PLACED SUCCESSFULLY")
            print(f"Order ID:     {result['orderId']}")
            print(f"Status:       {result['status']}")
            print(f"Executed Qty: {result['executedQty']}")
            print(f"Avg Price:    {result['avgPrice']}")
        else:
            print("🔴 ORDER FAILED")
            print(result["error"])
        print("="*40 + "\n")
        
    except ValueError as val_err:
        print(f"\n❌ Input Validation Error: {val_err}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Operational Error: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()