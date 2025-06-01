# CryptoBuddy/main.py

import requests
import json
import csv
from data_validator import update_crypto_energy_data, validate_crypto_db

API_KEY = 'your_coinmarketcap_api_key'  # Replace with your real key
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

params = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}

def get_sustainability_score(symbol):
    scores = {
        'BTC': 40,
        'ETH': 60,
        'ADA': 85,
        'SOL': 80,
        'XRP': 70
    }
    return scores.get(symbol.upper(), 60)

def main():
    response = requests.get(URL, headers=headers, params=params)
    data = response.json()

    crypto_db = {}

    for coin in data['data']:
        symbol = coin['symbol']
        crypto_db[symbol] = {
            'name': coin['name'],
            'symbol': symbol,
            'market_cap': coin['quote']['USD']['market_cap'],
            'price': coin['quote']['USD']['price'],
            'energy_usage_mwh_per_day': None,  # to be updated
            'sustainability_score': get_sustainability_score(symbol)
        }

    # Update energy usage using data_validator.py logic (live/manual hashrate)
    crypto_db = update_crypto_energy_data(crypto_db)

    # Save as JSON
    with open('crypto_db.json', 'w') as f:
        json.dump(crypto_db, f, indent=4)

    # Save as CSV
    with open('crypto_db.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Symbol', 'Name', 'Market Cap', 'Price', 'Energy Usage (MWh/day)', 'Sustainability Score'])
        for symbol, details in crypto_db.items():
            writer.writerow([
                symbol,
                details['name'],
                details['market_cap'],
                details['price'],
                details['energy_usage_mwh_per_day'],
                details['sustainability_score']
            ])

    # Run validation
    print("\nValidation Results:")
    results = validate_crypto_db(crypto_db)
    for sym, status in results.items():
        print(f"{sym}: {status}")

if __name__ == "__main__":
    main()
