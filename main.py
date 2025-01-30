import os
import requests
from twilio.rest import Client

# Load environment variables for security
STOCK_SYMBOL = os.environ.get("STOCK_SYMBOL", "TSLA")  # Default: TSLA
COMPANY_NAME = os.environ.get("COMPANY_NAME", "Tesla Inc")

# API Endpoints
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Fetch API keys from environment variables
STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# Twilio credentials from environment variables
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")  # Twilio WhatsApp Number
USER_PHONE_NUMBER = os.environ.get("USER_PHONE_NUMBER")  # User's WhatsApp Number

# Step 1: Fetch Stock Price Data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_API_URL, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]

# Extract the latest two days' closing prices
dates = list(stock_data.keys())
latest_date = dates[0]  # Most recent date
previous_date = dates[1]  # Day before

latest_close = float(stock_data[latest_date]["4. close"])
previous_close = float(stock_data[previous_date]["4. close"])

# Calculate the percentage change
price_change = latest_close - previous_close
price_change_percent = (abs(price_change) / latest_close) * 100

# Step 2: Fetch News If Price Change ≥ 5%
if price_change_percent >= 5:
    news_params = {
        "q": COMPANY_NAME,
        "from": latest_date,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_API_URL, params=news_params)
    news_data = news_response.json()["articles"][:3]  # Get top 3 news articles

    # Determine the price movement direction (🔺 or 🔻)
    price_direction = "🔺" if price_change > 0 else "🔻"

    # Step 3: Send WhatsApp Alerts via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in news_data:
        title = article["title"]
        description = article["description"]

        message_body = (
            f"{STOCK_SYMBOL}: {price_direction}{round(price_change_percent, 2)}%\n"
            f"Headline: {title}\n"
            f"Brief: {description}"
        )

        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message_body,
            to=USER_PHONE_NUMBER
        )

        print(f"Message Sent: {message.status}")
