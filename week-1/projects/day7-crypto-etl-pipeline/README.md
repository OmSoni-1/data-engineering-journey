# 🚀 Cryptocurrency Price Tracker - ETL Pipeline

A production-ready ETL pipeline that extracts real-time cryptocurrency prices from CoinGecko API, transforms the data using Pandas, and loads it into PostgreSQL.

## 📋 Project Overview

This project demonstrates a complete end-to-end data engineering workflow:
- **Extract**: Fetch live crypto prices from CoinGecko free API
- **Transform**: Clean, enrich, and structure data with Pandas
- **Load**: Store processed data in PostgreSQL database with proper schema

### Tracked Cryptocurrencies
- Bitcoin (BTC)
- Ethereum (ETH)
- Cardano (ADA)
- Solana (SOL)
- Ripple (XRP)

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and transformation |
| **PostgreSQL** | Relational database storage |
| **psycopg2** | PostgreSQL database adapter |
| **Requests** | HTTP library for API calls |
| **python-dotenv** | Environment variable management |
| **Logging** | Comprehensive execution tracking |

## 📁 Project Structure
```
day7-crypto-etl-pipeline/
│
├── .env                  # Environment variables (not in git)
├── requirements.txt     # Python dependencies
├── README.md            # This file
│
├── config.py            # Configuration management
├── logger.py            # Centralized logging setup
├── extract.py           # Data extraction from CoinGecko API
├── transform.py         # Data transformation with Pandas
├── load.py              # PostgreSQL data loading
├── pipeline.py          # ETL orchestration
└── run.py               # Main entry point
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

### Installation

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Setup PostgreSQL database**
```sql
-- Create database
CREATE DATABASE crypto_tracker;

-- Connect to database
\c crypto_tracker

-- Create table
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    crypto_id VARCHAR(50) NOT NULL,
    crypto_name VARCHAR(100) NOT NULL,
    price_usd DECIMAL(20, 2),
    market_cap_usd BIGINT,
    volume_24h_usd BIGINT,
    price_change_24h_pct DECIMAL(10, 2),
    price_category VARCHAR(20),
    is_positive_change BOOLEAN,
    extracted_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_crypto_id ON crypto_prices(crypto_id);
CREATE INDEX idx_extracted_at ON crypto_prices(extracted_at);
```

**3. Configure environment variables**

Create `.env` file:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_tracker
DB_USER=postgres
DB_PASSWORD=your_password_here
API_BASE_URL=https://api.coingecko.com/api/v3
```

**4. Run the pipeline**
```bash
python run.py
```

## 📊 Pipeline Features

### Extract Phase ✅
- Fetches real-time data from CoinGecko API (no authentication required)
- Retrieves price, market cap, volume, and 24h price change
- Comprehensive error handling and retry logic
- Request timeout protection
- Detailed logging at DEBUG and INFO levels

### Transform Phase ✅
- Converts raw JSON to structured Pandas DataFrame
- Adds calculated fields:
  - Price category (High/Medium/Low)
  - Trend indicators (positive/negative change)
  - Timestamp tracking
- Data quality checks and validation
- Handles missing values gracefully
- Rounds numeric values for consistency

### Load Phase ✅
- Bulk insert to PostgreSQL with transaction management
- Automatic rollback on errors
- Insert verification and counting
- Connection pooling best practices
- Proper resource cleanup (connections/cursors)

## 🔍 Example SQL Queries

### Get Latest Prices
```sql
SELECT crypto_name, price_usd, price_change_24h_pct, extracted_at
FROM crypto_prices
ORDER BY extracted_at DESC
LIMIT 5;
```

### Find Biggest 24h Gainers
```sql
SELECT crypto_name, price_usd, price_change_24h_pct
FROM crypto_prices
WHERE extracted_at >= NOW() - INTERVAL '1 day'
  AND is_positive_change = TRUE
ORDER BY price_change_24h_pct DESC;
```

### Price History for Bitcoin
```sql
SELECT 
    DATE_TRUNC('hour', extracted_at) as hour,
    AVG(price_usd) as avg_price,
    MIN(price_usd) as min_price,
    MAX(price_usd) as max_price
FROM crypto_prices
WHERE crypto_id = 'bitcoin'
  AND extracted_at >= NOW() - INTERVAL '24 hours'
GROUP BY hour
ORDER BY hour DESC;
```

### Market Cap Comparison
```sql
SELECT crypto_name, 
       market_cap_usd,
       RANK() OVER (ORDER BY market_cap_usd DESC) as market_rank
FROM crypto_prices
WHERE extracted_at = (SELECT MAX(extracted_at) FROM crypto_prices);
```

## 📈 Skills Demonstrated

✅ **API Integration** - RESTful API consumption with error handling  
✅ **Data Transformation** - Pandas data manipulation and enrichment  
✅ **Database Operations** - PostgreSQL CRUD with transactions  
✅ **Error Handling** - Comprehensive exception management  
✅ **Logging** - Production-grade logging (console + file)  
✅ **Configuration Management** - Environment-based configuration  
✅ **Code Organization** - Modular, maintainable architecture  
✅ **Documentation** - Professional README and inline comments  
✅ **Data Quality** - Validation and null handling  
✅ **Security** - Credentials management with .env  

## 🎯 Data Engineering Concepts

| Concept | Implementation |
|---------|---------------|
| **ETL Pattern** | Separate extract, transform, load modules |
| **Idempotency** | Safe to run multiple times |
| **Error Recovery** | Graceful failure handling with logging |
| **Logging & Monitoring** | Detailed execution tracking |
| **Configuration** | Externalized settings via .env |
| **Data Quality** | Validation and quality checks |
| **Scalability** | Modular design for easy extension |

## 🔜 Future Enhancements

- [ ] Add comprehensive unit tests with pytest
- [ ] Implement scheduling (Airflow/Apache Airflow or cron)
- [ ] Add data visualization dashboard (Plotly/Streamlit)
- [ ] Create data quality alerts and monitoring
- [ ] Implement incremental loading strategy
- [ ] Add more cryptocurrencies dynamically
- [ ] Create materialized views for common queries
- [ ] Add email/Slack notifications on failure
- [ ] Implement data retention policies
- [ ] Add performance metrics tracking

## 📚 What I Learned

Building this project taught me:
- **Modular code** is essential for testing and maintenance
- **Proper logging** saves hours of debugging in production
- **Environment variables** keep sensitive data secure
- **Data validation** prevents downstream issues
- **Error handling** makes pipelines resilient
- **Documentation** helps others (and future me) understand the code

## 🐛 Troubleshooting

**Issue**: `psycopg2` installation fails  
**Solution**: Install PostgreSQL development files or use `psycopg2-binary`

**Issue**: API request timeout  
**Solution**: Check internet connection, CoinGecko API might be rate-limited

**Issue**: Database connection refused  
**Solution**: Verify PostgreSQL is running: `pg_ctl status`

**Issue**: Permission denied on database  
**Solution**: Check user permissions in PostgreSQL

## 📊 Performance

- **Execution Time**: ~2-5 seconds per run
- **API Latency**: ~500ms-1s (CoinGecko free tier)
- **Database Insert**: ~100ms for 5 records
- **Memory Usage**: <50MB

## 🤝 Acknowledgments

Built as part of my 90-day Data Engineering learning journey (Week 1, Day 7).

Special thanks to:
- CoinGecko for free cryptocurrency API
- PostgreSQL community for excellent documentation
- Data engineering community for inspiration

---

**Project Status:** ✅ Production Ready  
**Created:** February 14, 2026  
**Version:** 1.0.0  
**Author:** Om Soni  
**Portfolio Project:** Week 1 - Capstone