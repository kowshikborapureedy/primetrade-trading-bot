def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    # Standardize to uppercase for API compatibility
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.") [cite: 18, 21]
        
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError(f"Invalid order type '{order_type}'. Must be MARKET or LIMIT.") [cite: 17, 22]
        
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.") [cite: 23]
        
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("Price is required and must be greater than 0 for LIMIT orders.") [cite: 24]
        
    return symbol, side, order_type, quantity, price