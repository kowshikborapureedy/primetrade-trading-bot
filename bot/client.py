import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_binance_client():
    # Read the keys securely from your .env file variable names
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("API Keys missing! Please set them in your .env file.")
        
    client = Client(api_key, api_secret)
    
    # Force python-binance to use the correct unified Demo trading endpoint urls
    client.FUTURES_URL = 'https://demo-fapi.binance.com/fapi'
    client.FUTURES_TESTNET_URL = 'https://demo-fapi.binance.com/fapi'
    
    return client