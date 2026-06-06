import smtplib
import requests
import os
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "8bf0e9aa090e4c9e8e8e1336197afd35"

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

alphavantage_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}

news_param = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

response = requests.get(ALPHAVANTAGE_URL, params=alphavantage_param)
response.raise_for_status()
stock_data = response.json()

# FIX 1: Turn the dictionary values into a list to pull the 2 most recent active market days dynamically
# This completely bypasses the weekend/holiday KeyError crash!
time_series = stock_data["Time Series (Daily)"]
data_list = [value for (key, value) in time_series.items()]

yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

# FIX 2: Calculate the real percentage difference and pick the right emoji
price_diff = yesterday_close - day_before_close
percentage_diff = (price_diff / day_before_close) * 100
up_down_emoji = "🔺" if price_diff > 0 else "🔻"

# Check if price moved by 1% or more
if abs(percentage_diff) >= 1.0:
    response2 = requests.get(NEWS_URL, params=news_param)
    response2.raise_for_status()
    news_data = response2.json()
    articles = news_data["articles"]
    top_headlines = articles[0:3]

    # FIX 2 (cont.): Format strings exactly like the project prompt guidelines
    formatted_articles = [
        f"Subject: {STOCK}: {up_down_emoji}{abs(percentage_diff):.0f}%\n\n"
        f"Headline: {article['title']}.\n"
        f"Brief: {article['description']}"
        for article in top_headlines
    ]

    # Optimization: Keep the SMTP connection open outside the loop instead of reconnecting 3 times
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        for article in formatted_articles:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                # FIX 3: Encode to utf-8 so the email server processes the up/down emojis without breaking
                msg=article.encode("utf-8"),
            )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

