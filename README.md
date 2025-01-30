# Stock-Alert-and-News-App

### 📌 Project Overview
Stock Alert and News App is a Python-based automation tool that monitors stock price changes and sends real-time alerts. It uses **Alpha Vantage API** to track stock price fluctuations, **News API** to fetch relevant news, and **Twilio API** to deliver notifications via WhatsApp when a significant stock change occurs (≥5%).  

### 🚀 Features  
✅ Monitors stock closing prices and detects changes of **≥5%**  
✅ Fetches **top 3 latest news headlines & summaries** related to the stock  
✅ Sends stock change alerts and news updates **directly to WhatsApp** using Twilio API  
✅ Fully automated and **real-time stock tracking**  

### 🛠 Tech Stack  
- **Programming Language:** Python  
- **APIs Used:**  
  - [Alpha Vantage API](https://www.alphavantage.co/) – For fetching stock price data  
  - [News API](https://newsapi.org/) – For retrieving top news articles  
  - [Twilio API](https://www.twilio.com/) – For sending WhatsApp notifications  
- **Libraries:** `requests`, `json`, `datetime`, `twilio`, `dotenv`  

### 📌 Installation & Setup  

#### 1️⃣ Clone the repository  
        git clone https://github.com/Vikkram-V/stock-alert-news-app.git
        cd stock-alert-news-app
        
#### 2️⃣ Set up API keys  
Create a `.env` file and add your API keys:  

# Stock & News APIs
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key

# Twilio Credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=whatsapp:+14155238886  # Twilio WhatsApp sandbox number
USER_PHONE_NUMBER=whatsapp:+919875618970  # Your WhatsApp number

# Stock Details
STOCK_SYMBOL=TSLA
COMPANY_NAME=Tesla Inc

#### 3️⃣ Run the script 

        python main.py

### 📌 Example Output
If the stock price changes by more than 5%, you receive a WhatsApp message like:  

TSLA: 🔺6%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

TSLA: 🔻6%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

TSLA: 🔻8%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

### 📌 Future Enhancements  
🔹 Support for **multiple stocks**  
🔹 Custom alerts for **different percentage thresholds**  
🔹 Integration with **email notifications**  
