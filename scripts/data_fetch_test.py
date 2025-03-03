!pip install yfinance

import yfinance as yf

# Fetch stock data for Apple
ticker = "AAPL"
stock_data = yf.Ticker(ticker)

# Get historical market data
apple_data = stock_data.history(period="1y")  # Options: "1d", "5d", "1mo", "1y", etc.

# Display the first few rows
apple_data.head()

# Fetch stock data for Google
ticker = "GOOGL"
stock_data = yf.Ticker(ticker)

# Get historical market data
google_data = stock_data.history(period="1mo")  # Options: "1d", "5d", "1mo", "1y", etc.

# Display the first few rows
google_data.head()

# Fetch stock data for Google
ticker = "MSFT"
stock_data = yf.Ticker(ticker)

# Get historical market data
microsoft_data = stock_data.history(period="1mo")  # Options: "1d", "5d", "1mo", "1y", etc.

# Display the first few rows
microsoft_data.head()

# Fetch stock data for Meta
ticker = "META"
stock_data = yf.Ticker(ticker)

# Get historical market data
meta_data = stock_data.history(period="1mo")  # Options: "1d", "5d", "1mo", "1y", etc.

# Display the first few rows
meta_data.head()

# Fetch stock data for Tesla
ticker = "TSLA"
stock_data = yf.Ticker(ticker)

# Get historical market data
meta_data = stock_data.history(period="1mo")  # Options: "1d", "5d", "1mo", "1y", etc.

# Display the first few rows
meta_data.head()
