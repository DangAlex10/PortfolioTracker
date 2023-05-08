import pytest
from unittest.mock import Mock
from functions import get_data, get_chart


@pytest.fixture
def mock_yf_ticker(mocker):
    mock = mocker.patch("yfinance.Ticker")
    mock.return_value.info = {
        'longName': 'Apple Inc.',
        'regularMarketPrice': 130.21,
        'regularMarketChange': 2.32,
        'regularMarketChangePercent': 1.81,
        'marketCap': 2200000000000,
        'regularMarketVolume': 10000000
    }
    return mock

print('hello')
@pytest.mark.usefixtures("mock_yf_ticker")
def test_get_data():
    data = get_data('AAPL')
    assert data['symbol'] == 'AAPL'
    assert data['name'] == 'Apple Inc.'
    assert data['price'] == '130.21'
    assert data['change'] == 2.32
    assert data['percent_change'] == '1.81'
    assert data['market_cap'] == '2.20 trillion'
    assert data['volume'] == '10.00 million'