# content of test_functions.py

from functions import get_data

def test_get_data_valid_symbol():
    symbol = 'AAPL' # Apple Inc. stock symbol
    data = get_data(symbol)
    assert data['symbol'] == symbol
    assert data['name'] == 'Apple Inc.'
    assert data['price'][0] == '$'
    assert data['change'] is not None
    assert data['percent_change'][-1] == '%'
    assert data['market_cap'] is not None
    assert data['volume'] is not None

def test_get_data_invalid_symbol():
    symbol = 'INVALID'
    data = get_data(symbol)
    assert data['symbol'] == symbol
    assert data['name'] is None
    assert data['price'] is None
    assert data['change'] is None
    assert data['percent_change'] is None
    assert data['market_cap'] is None
    assert data['volume'] is None