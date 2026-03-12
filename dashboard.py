import pandas as pd
import yfinance as yf
import plotly.express as px

# list of companies
tickers = ["AAPL","MSFT","AMZN","GOOGL"]

# download stock data
data = yf.download(tickers, start="2020-01-01")

# closing prices
prices = data["Close"]

print("Stock price data:")
print(prices.tail())

# calculate returns
returns = prices.pct_change()

# calculate volatility (risk)
volatility = returns.std()

print("\nVolatility (risk levels):")
print(volatility)

# price comparison chart
fig = px.line(prices,
              title="Stock Price Comparison: Apple vs Major Tech Companies")

fig.show()

# volatility chart
fig2 = px.bar(volatility,
              title="Volatility Comparison (Financial Risk)")

fig2.show()
