import logging
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

def execute_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Sending order request: {side} {order_type} {quantity} {symbol} " + (f"@ {price}" if price else ""))
        
        if order_type == 'MARKET':
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
        elif order_type == 'LIMIT':
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',  # Good 'Till Cancelled
                quantity=quantity,
                price=price
            )
            
        logger.info(f"Order successfully executed. Order ID: {response.get('orderId')}")
        return {
            "success": True,
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }
        
    except BinanceAPIException as e:
        error_msg = f"Binance API Error: Status Code {e.status_code}, Message: {e.message}"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}
    except Exception as e:
        error_msg = f"Unexpected Failure: {str(e)}"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}