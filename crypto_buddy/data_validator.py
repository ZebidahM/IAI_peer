import requests

# Crypto database with manual hashrate data (in TH/s) as fallback
crypto_db = {
    "bitcoin": {
        "symbol": "BTC",
        "name": "Bitcoin",
        "manual_hashrate_ths": 150_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "ethereum": {
        "symbol": "ETH",
        "name": "Ethereum",
        "manual_hashrate_ths": 900_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "cardano": {
        "symbol": "ADA",
        "name": "Cardano",
        "manual_hashrate_ths": 10_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "solana": {
        "symbol": "SOL",
        "name": "Solana",
        "manual_hashrate_ths": 50_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "ripple": {
        "symbol": "XRP",
        "name": "Ripple",
        "manual_hashrate_ths": 5_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "polkadot": {
        "symbol": "DOT",
        "name": "Polkadot",
        "manual_hashrate_ths": 20_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "litecoin": {
        "symbol": "LTC",
        "name": "Litecoin",
        "manual_hashrate_ths": 500_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "chainlink": {
        "symbol": "LINK",
        "name": "Chainlink",
        "manual_hashrate_ths": 100_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    },
    "dogecoin": {
        "symbol": "DOGE",
        "name": "Dogecoin",
        "manual_hashrate_ths": 200_000,  # Example manual hashrate value
        "sustainability_score": None,
        "energy_usage_mwh_per_day": None,
    }
}

def get_live_hashrate(coin_id):
    """
    Fetch the current network hashrate (TH/s) from CoinGecko API.
    Returns None if data is not found.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Placeholder: CoinGecko does not provide hashrate, so return None
        return None

    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching hashrate for {coin_id}: {e}")
        return None


def estimate_energy_usage_from_hashrate(hashrate_ths, power_per_ths=50):
    """
    Estimate daily energy usage (MWh) from network hashrate.
    """
    if hashrate_ths is None or hashrate_ths <= 0:
        return None

    total_power_watts = hashrate_ths * power_per_ths * 1e12  # Convert TH/s to H/s for watts calculation
    seconds_per_day = 24 * 60 * 60
    energy_wh_per_day = total_power_watts * seconds_per_day
    energy_mwh_per_day = energy_wh_per_day / 1e6  # Convert to MWh

    return energy_mwh_per_day


def update_crypto_energy_data(db):
    """
    Update crypto database energy usage field using live or manual hashrate.
    """
    for coin_id, info in db.items():
        hashrate = get_live_hashrate(coin_id)

        if hashrate is None:
            # Use manual fallback if live data not available
            hashrate = info.get("manual_hashrate_ths")

        energy_usage = estimate_energy_usage_from_hashrate(hashrate)
        db[coin_id]['energy_usage_mwh_per_day'] = energy_usage

    return db


def validate_crypto_db(crypto_db):
    """
    Validates the crypto_db dictionary.
    Returns a dict mapping symbol -> validation status message.
    """
    results = {}

    for symbol, data in crypto_db.items():
        errors = []

        # Check required fields
        required_fields = ['name', 'symbol', 'market_cap', 'price', 'energy_usage_mwh_per_day', 'sustainability_score']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing field: {field}")
            elif data[field] is None:
                errors.append(f"Field {field} is None")

        # Check data types
        if 'market_cap' in data and data['market_cap'] is not None:
            if not isinstance(data['market_cap'], (int, float)):
                errors.append("market_cap should be a number")

        if 'price' in data and data['price'] is not None:
            if not isinstance(data['price'], (int, float)):
                errors.append("price should be a number")

        if 'energy_usage_mwh_per_day' in data and data['energy_usage_mwh_per_day'] is not None:
            if not isinstance(data['energy_usage_mwh_per_day'], (int, float)):
                errors.append("energy_usage_mwh_per_day should be a number")

        if 'sustainability_score' in data and data['sustainability_score'] is not None:
            if not isinstance(data['sustainability_score'], (int, float)):
                errors.append("sustainability_score should be a number")

        if errors:
            results[symbol] = "Invalid: " + "; ".join(errors)
        else:
            results[symbol] = "Valid"

    return results


if __name__ == "__main__":
    updated_db = update_crypto_energy_data(crypto_db)
    for coin, data in updated_db.items():
        print(f"{data['name']} ({data['symbol']}): Energy Usage = {data['energy_usage_mwh_per_day']} MWh/day")
