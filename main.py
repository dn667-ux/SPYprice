import yfinance as yf
import requests
import os

WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1468337671041581168/vII1Ke1qLMf_Cus3D7j51puPUShPTNU574Zs7E5VxmGEIQ4qT5Eyx9KVfHDNCZpcFvvU")
SYMBOL = "SPY"

def send_price(price):
    data = {
        "embeds": [{
            "title": "📊 SPY Price Update",
            "color": 0x3498db,
            "fields": [
                {"name": "Symbol", "value": SYMBOL, "inline": True},
                {"name": "Price", "value": f"{price:.2f}", "inline": True}
            ]
        }]
    }
    requests.post(WEBHOOK_URL, json=data)

def get_price():
    df = yf.download(
        SYMBOL,
        period="1d",
        interval="1m",
        progress=False
    )
    if df.empty:
        return None
    return df["Close"].iloc[-1]

if __name__ == "__main__":
    price = get_price()
    if price:
        send_price(price)
