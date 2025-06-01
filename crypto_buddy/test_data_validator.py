import unittest
from data_validator import validate_crypto_db

class TestValidateCryptoDB(unittest.TestCase):

    def test_valid_crypto_db(self):
        crypto_db = {
            'BTC': {
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'market_cap': 600_000_000_000,
                'price': 30000,
                'energy_usage_mwh_per_day': 1000000,
                'sustainability_score': 40
            }
        }
        results = validate_crypto_db(crypto_db)
        self.assertEqual(results['BTC'], "Valid")

    def test_missing_fields(self):
        crypto_db = {
            'ETH': {
                'name': 'Ethereum',
                'symbol': 'ETH',
                # missing market_cap, price
                'energy_usage_mwh_per_day': 500000,
                'sustainability_score': 60
            }
        }
        results = validate_crypto_db(crypto_db)
        self.assertTrue('Missing field: market_cap' in results['ETH'])
        self.assertTrue('Missing field: price' in results['ETH'])

    def test_none_fields(self):
        crypto_db = {
            'ADA': {
                'name': 'Cardano',
                'symbol': 'ADA',
                'market_cap': None,
                'price': 1.5,
                'energy_usage_mwh_per_day': 2000,
                'sustainability_score': None
            }
        }
        results = validate_crypto_db(crypto_db)
        self.assertTrue('Field market_cap is None' in results['ADA'])
        self.assertTrue('Field sustainability_score is None' in results['ADA'])

    def test_wrong_types(self):
        crypto_db = {
            'SOL': {
                'name': 'Solana',
                'symbol': 'SOL',
                'market_cap': 'not a number',
                'price': 30,
                'energy_usage_mwh_per_day': 500,
                'sustainability_score': 80
            }
        }
        results = validate_crypto_db(crypto_db)
        self.assertTrue('market_cap should be a number' in results['SOL'])

if __name__ == "__main__":
    unittest.main()
