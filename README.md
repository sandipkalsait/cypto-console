
# Crypto-Console

Crypto-Console is a Python-based cryptocurrency data analysis tool that uses the CoinMarketCap API to fetch and filter cryptocurrency data based on specific criteria. It also provides basic technical indicator alerts (like RSI) to aid in investment decisions.

---

## Features

- Fetch real-time cryptocurrency data from CoinMarketCap.
- Filter coins based on market cap, price, and liquidity.
- Calculate technical indicators like RSI (Relative Strength Index).
- Generate alerts for buy or sell opportunities based on RSI thresholds.
- Display results in a user-friendly table format.

---

## Prerequisites

Before running the application, ensure the following dependencies are installed:

- Python 3.7 or later
- Required Python libraries:
  - `requests`
  - `pandas`
  - `tabulate`

Install dependencies using:
```
pip install requests pandas tabulate
```

---

## Usage

1. Replace `YOUR API KEY` in the script with your CoinMarketCap API key.
2. Run the script using:
```
python crypto_console.py
```
3. The application will fetch cryptocurrency data, filter it based on predefined criteria, and display results along with RSI-based alerts.

---

## Customization

- **Filtering Criteria**: Modify the parameters in `get_filtered_coins()` function to set custom market cap, price, and liquidity thresholds.
- **RSI Alerts**: Adjust the `min_rsi` and `max_rsi` values in the `alert_system()` function for personalized alert levels.

---

## Example Output

Filtered Results:
```
+----------+--------+-------------+-------------+-----------------+------------------+----------------+---------------------+-------------+
| Name     | Symbol | Market Cap  | Price (USD) | 24h Volume (USD)| 24h Change (%)   | Liquidity (USD)| Launch Date         | Quantity    |
+----------+--------+-------------+-------------+-----------------+------------------+----------------+---------------------+-------------+
| Bitcoin  | BTC    | 900000000000| 45000       | 32000000000     | 2.5              | 850000000000   | 2013-04-28          | 21000000    |
+----------+--------+-------------+-------------+-----------------+------------------+----------------+---------------------+-------------+
```

Technical Indicators (RSI) Alerts:
```
Alert: Bitcoin (BTC) RSI is above 70. Consider selling.
```

---

## Disclaimer

This tool is for informational purposes only and does not constitute financial advice. Please perform your own research before making investment decisions.

---

## License

Crypto-Console is released under the MIT License.
