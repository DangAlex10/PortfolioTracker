import pytest
from unittest import mock
from django.test import TestCase
from webpage.views import get_chart
from webpage.views import get_data

def test_get_chart_with_valid_symbol():
    # Mock the yfinance Ticker object
    mock_ticker = mock.Mock()
    mock_ticker.history.return_value = {
        'Open': [100, 110, 105],
        'High': [120, 115, 125],
        'Low': [95, 100, 100],
        'Close': [110, 105, 115],
        'Volume': [1000, 2000, 1500]
    }
    mock_ticker.info = {'longName': 'Mock Stock'}
    with mock.patch('webpage.views.yf.Ticker', return_value=mock_ticker):
        chart = get_chart('MSFT')
    assert chart is not None
    assert 'Mock Stock Stock Chart' in chart
    assert 'Closing Price' in chart

def test_get_chart_with_invalid_symbol():
    with pytest.raises(Exception) as e:
        get_chart('INVALID')
    assert str(e.value) == 'No data found, symbol may be delisted'

def test_get_chart_with_missing_symbol():
    with pytest.raises(Exception) as e:
        get_chart(None)
    assert str(e.value) == 'Symbol is required'

def test_get_data_with_valid_symbol():
    # Mock the yfinance Ticker object
    mock_ticker = mock.Mock()
    mock_ticker.info = {
        'longName': 'Mock Stock',
        'regularMarketPrice': 123.45,
        'regularMarketChange': 1.23,
        'regularMarketChangePercent': 0.99,
        'marketCap': 1000000000,
        'regularMarketVolume': 1000000
    }
    with mock.patch('webpage.views.yf.Ticker', return_value=mock_ticker):
        data = get_data('MSFT')
    assert data is not None
    assert data['symbol'] == 'MSFT'
    assert data['name'] == 'Mock Stock'
    assert data['price'] == '$123.45'
    assert data['change'] == 1.23
    assert data['percent_change'] == '0.99%'
    assert data['market_cap'] == '1B'
    assert data['volume'] == '1M'

def test_get_data_with_invalid_symbol():
    with pytest.raises(Exception) as e:
        get_data('INVALID')
    assert str(e.value) == 'No data found, symbol may be delisted'

def test_get_data_with_missing_symbol():
    with pytest.raises(Exception) as e:
        get_data(None)
    assert str(e.value) == 'Symbol is required'