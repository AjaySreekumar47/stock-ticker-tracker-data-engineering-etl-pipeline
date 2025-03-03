import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd
import os
import requests

# Initialize S3 client
s3 = boto3.client("s3")
BUCKET_NAME = "stockmarketticker-bucket"  
API_KEY = os.environ.get('API_KEY')
SYMBOLS = ["AAPL", "GOOGL", "MSFT", "META", "TSLA"]
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol):
    """Fetch daily stock data from Alpha Vantage."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
    return None

def save_to_s3(data, symbol):
    """Save stock data to an S3 bucket as a CSV file."""
    df = pd.DataFrame.from_dict(data, orient="index")
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Date"}, inplace=True)

    # Convert columns to numeric (Alpha Vantage returns strings)
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Define S3 folder paths
    folder_mapping = {
        "AAPL": "Apple/",
        "GOOGL": "Google/",
        "MSFT": "Microsoft/",
        "META": "Meta/",
        "TSLA": "Tesla/"
    }

    if symbol in folder_mapping:
        folder = folder_mapping[symbol]
    else:
        folder = "processed_data/"  

    # Generate file path
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"{folder}{symbol}_{timestamp}.csv"

    # Convert DataFrame to CSV
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    # Upload to S3
    s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=csv_buffer.getvalue())

    return f"Saved {symbol} data to {file_path} in S3"

def lambda_handler(event, context):
    results = {}
    
    for symbol in SYMBOLS:
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            s3_path = save_to_s3(stock_data, symbol)
            results[symbol] = s3_path
        else:
            results[symbol] = "Failed to fetch data"

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }
