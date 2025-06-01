## Team contribution

Ohachor Daniel - pushed from Danchi-1 repo
---
As the Data Management & Research Specialist, my primary focus was on building and validating the crypto database that powers CryptoBuddy's decision-making.
I used the CoinMarketCap API to collect real-time data on market prices and market caps for leading cryptocurrencies (main.py). To help our chatbot make responsible investment suggestions, I added sustainability scores to each coin based on factors like energy usage and consensus mechanism (e.g., Proof of Work vs. Proof of Stake). These scores were manually assigned based on external research and can be improved further with live energy data in future versions.
To ensure data quality, I built a validation module (data_validator.py) that checks each entry in the database for structure, missing fields, and data type accuracy. This ensures the chatbot logic receives clean and consistent inputs.
The final crypto_db is saved in both JSON and CSV formats and can be easily queried or updated as needed.
---

# crypto_buddy

Example user interaction:
User: Which crypto is trending?
CryptoBuddy: 🔥 These cryptos are on the rise: Bitcoin, Cardano, Solana!
--------------------------------------
User: What’s the most sustainable coin?
CryptoBuddy: 🌱 Invest in Algorand! It's eco-friendly with a strong future.
--------------------------------------
User: How does crypto work?
CryptoBuddy: Crypto uses decentralized blockchain technology to verify transactions securely
