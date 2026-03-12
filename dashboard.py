import pandas as pd
import yfinance as yf
import plotly.express as px

# companies to analyse
tickers = ["AAPL","MSFT","AMZN","GOOGL"]

# download stock data
data = yf.download(tickers, start="2020-01-01")

# closing prices
prices = data["Close"]

print(prices.tail())

# calculate returns
returns = prices.pct_change()

# calculate volatility (risk)
volatility = returns.std()

print(volatility)

# price chart
fig = px.line(prices,
              title="Stock Price Comparison: Apple vs Microsoft vs Amazon vs Google")

fig.show()

# risk chart
fig2 = px.bar(volatility,
              title="Volatility Comparison")

fig2.show()
