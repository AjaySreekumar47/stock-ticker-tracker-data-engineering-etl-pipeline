# Stock ticker tracker data engineering etl pipeline

## Overview
This project provides an ETL pipeline that pulls stock data from 5 popular stock tickers using the Alpha Vantage API - processes it, and stores it in Amazon S3 for analysis. The pipeline is built using AWS services like Lambda, Glue, Athena, and S3, with automated triggers and crawlers for seamless data integration.

## Features
- **Data Retrieval:** Uses the **Alpha Vantage API** to fetch financial data.
- **Data Storage:** Stores raw and processed data in **Amazon S3**. Used **Amazon CloudWatch** for extracting data every 2 minutes for this project.
- **Data Transformation:** Leverages **AWS Glue** for data transformation and cleaning upon raw data extraction from API.
- **Data Analysis:** Uses **AWS Athena** for querying the transformed data.
- **Automation:** **AWS Lambda** functions are triggered automatically for data fetching and processing.

## WorkFlow

<img width="496" alt="image" src="https://github.com/user-attachments/assets/a51ec6eb-cffc-45fd-b7c7-f870ee180b98" />



<img width="733" alt="image" src="https://github.com/user-attachments/assets/2f35e5e6-2bf5-410e-8469-34db72f187e4" />

## Getting Started
### Prerequisites
AWS account with necessary services (S3, Lambda, Glue, Athena)
Alpha Vantage API key
Python 3.x (for local testing)
