import requests

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "low",
        "sustainability_score": 0.9
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.7
    },
    "Avalanche": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 0.6
    },
    "Litecoin": {
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "high",
        "sustainability_score": 0.4
    },
    "Chainlink": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    },
    "Algorand": {
        "price_trend": "rising",
        "market_cap": "low",
        "energy_use": "very low",
        "sustainability_score": 0.9
    }
}

def recommend_crypto(strategy="balanced"):
    """Recommend cryptocurrencies based on strategy: profitability, sustainability, or balanced."""
    if strategy == "profitability":
        recommended = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    elif strategy == "sustainability":
        recommended = [coin for coin, data in crypto_db.items() if data["energy_use"] in ["low", "very low"] and data["sustainability_score"] >= 0.7]
    else:
        # Balanced: prefer high sustainability among profitable cryptos
        profitable = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        recommended = sorted(profitable, key=lambda x: crypto_db[x]["sustainability_score"], reverse=True)[:3]

    return f"🔍 Recommended Cryptos: {', '.join(recommended)}"

def parse_user_query(user_input):
    """Determine user's intent based on keywords."""
    keywords = user_input.lower().split()
    if "sustainable" in keywords or "eco-friendly" in keywords:
        return recommend_crypto(strategy="sustainability")
    elif "profit" in keywords or "trending" in keywords:
        return recommend_crypto(strategy="profitability")
    elif "growth" in keywords or "long-term" in keywords:
        return recommend_crypto(strategy="balanced")
    else:
        return "🤖 I'm not sure! Try asking about sustainability or profitability."

def validate_input(user_input):
    """Checks if user input contains valid keywords."""
    valid_keywords = ["trending", "sustainable", "investment", "crypto", "profit", "eco-friendly", "growth", "long-term"]
    return any(keyword in user_input.lower() for keyword in valid_keywords)

def chatbot_response(user_input):
    """Provides recommendations or prompts user for better queries."""
    if validate_input(user_input):
        return parse_user_query(user_input)
    else:
        return "🤔 I didn't quite get that. Try asking about trends or sustainability!"

def fetch_real_time_data(crypto_name):
    """Gets latest price trends and market details from CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name.lower()}&vs_currencies=usd"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()[crypto_name.lower()]["usd"]
        else:
            return "Error fetching data."
    except:
        return "Error connecting to API."
