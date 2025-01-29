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
        git clone https://github.com/yourusername/stock-alert-news-app.git
        cd stock-alert-news-app
        
#### 2️⃣ Install dependencies  

        pip install -r requirements.txt

#### 3️⃣ Set up API keys  
Create a `.env` file and add your API keys:  

ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
USER_PHONE_NUMBER=your_whatsapp_number
STOCK_SYMBOL=TSLA  # Example stock symbol

#### 4️⃣ Run the script 

        python main.py

### 📌 Example Output
If the stock price changes by more than 5%, you receive a WhatsApp message like:  

📈 Tesla Stock Alert 🚀  
TSLA stock price changed by +5.2% today!  

📰 Top News:  
1️⃣ Tesla launches new EV model in 2024...  
2️⃣ Elon Musk announces AI-driven stock predictions...  
3️⃣ Tesla stocks hit a record high this quarter...  


### 📌 Future Enhancements  
🔹 Support for **multiple stocks**  
🔹 Custom alerts for **different percentage thresholds**  
🔹 Integration with **email notifications**  

