import requests
import pandas as pd
from tabulate import tabulate

# Your CoinMarketCap API key
API_KEY = 'YOUR API KEY'

# CoinMarketCap API endpoint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Request headers
headers = {
    'Accept': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

# Define the filtering criteria
def get_filtered_coins(min_market_cap=0, max_price=float('inf'), min_liquidity=0):
    parameters = {
        'start': '1',
        'limit': '100',  # You can adjust this limit
        'convert': 'USD'
    }
    
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()['data']

    # Filtering coins based on the specified criteria
    filtered_coins = []
    for coin in data:
        market_cap = coin['quote']['USD']['market_cap']
        price = coin['quote']['USD']['price']

        # Safely check if total_supply exists
        total_supply = coin.get('circulating_supply', 0)  # Use circulating_supply as an alternative
        liquidity = total_supply * price  # Approximation for liquidity

        if market_cap >= min_market_cap and price <= max_price and liquidity >= min_liquidity:
            filtered_coins.append({
                'Name': coin['name'],
                'Symbol': coin['symbol'],
                'Market Cap': market_cap,
                'Price (USD)': price,
                '24h Volume (USD)': coin['quote']['USD']['volume_24h'],
                '24h Change (%)': coin['quote']['USD']['percent_change_24h'],
                'Liquidity (USD)': liquidity,
                'Launch Date': coin['date_added'],
                'Quantity': total_supply  # Use circulating_supply as quantity
            })

    return filtered_coins


# Calculate RSI (Relative Strength Index)
def calculate_rsi(prices, period=14):
    gains = []
    losses = []
    
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change >= 0:
            gains.append(change)
            losses.append(0)
        else:
            losses.append(-change)
            gains.append(0)
    
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Alert system
def alert_system(coin_data, min_rsi=30, max_rsi=70):
    alerts = []
    for coin in coin_data:
        rsi = calculate_rsi([coin['Price (USD)']]*14)  # RSI needs real historical data for accuracy
        if rsi < min_rsi:
            alerts.append(f"Alert: {coin['Name']} ({coin['Symbol']}) RSI is below {min_rsi}. Consider buying.")
        elif rsi > max_rsi:
            alerts.append(f"Alert: {coin['Name']} ({coin['Symbol']}) RSI is above {max_rsi}. Consider selling.")
    return alerts

# Display the results
def display_results(filtered_coins):
    df = pd.DataFrame(filtered_coins)
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

# Main function to run the program
def main():
    print("Fetching and filtering cryptocurrencies...\n")
    filtered_coins = get_filtered_coins(min_market_cap=500000000, max_price=500, min_liquidity=100000000)
    
    if filtered_coins:
        print("Filtered Results:")
        display_results(filtered_coins)
        print("\nTechnical Indicators (RSI) Alerts:")
        alerts = alert_system(filtered_coins)
        for alert in alerts:
            print(alert)
    else:
        print("No coins match the given filters.")

# Run the program
if __name__ == "__main__":
    main()
