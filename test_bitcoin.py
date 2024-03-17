import unittest
from unittest import TestCase
from unittest.mock import patch, call
from bitcoin import url
import bitcoin

class TestBitcoin(TestCase):

    @patch('builtins.print')
    def test_print_current_rate(self, mock_print):
        bitcoin.print_current_rate(9999.9999)
        mock_print.assert_called_once_with('The rate of the USD is $9999.9999.')

    @patch('builtins.print')
    def test_print_total(self, mock_print):
        bitcoin.print_total(123456.789)
        mock_print.assert_called_once_with('The total amount of USD you have in bitcoin is $123456.789.')

    def test_rate_from_api(self):
        expected_rate = 62787.9728

        example_api_response = {'time': {'updated': 'Mar 1, 2024 23:21:35 UTC', 'updatedISO': '2024-03-01T23:21:35+00:00', 'updateduk': 'Mar 1, 2024 at 23:21 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '62,787.973', 'description': 'United States Dollar', 'rate_float': 62787.9728}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '49,607.333', 'description': 'British Pound Sterling', 'rate_float': 49607.3332}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '57,893.65', 'description': 'Euro', 'rate_float': 57893.6504}}}

        rate_result = bitcoin.get_rate_from_response(example_api_response)
        self.assertEqual(expected_rate, rate_result)

    def test_get_bitcoin_input(self):
        result = bitcoin.get_bitcoins('5.0', 5.0)
        self.assertEqual(result, 5.0)

    def test_calculate_bitcoin_total(self):
        result = bitcoin.calculate_bitcoin_total(5, 5)
        self.assertEqual(result, 25)

    def test_make_api_request(self):
        (result, error) = bitcoin.make_api_request(url)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()