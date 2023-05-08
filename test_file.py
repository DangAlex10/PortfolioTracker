# content of test_functions.py

from functions import get_data

def test_get_data_valid_symbol():
    symbol = 'AAPL' # Apple Inc. stock symbol
    data = get_data(symbol)
    assert data['symbol'] == symbol


def test_get_data_invalid_symbol():
    symbol = 'INVALID'
    data = get_data(symbol)
    assert data['symbol'] == symbol
