import pytest
import json
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch
import yfinance as yf
import plotly.graph_objs as go
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

@patch('functions.yf.Ticker')
def test_get_chart(mock_yf_ticker):
    # Set up the mock object
    mock_stock_data = {
        'Open': [100, 150, 200],
        'High': [125, 175, 225],
        'Low': [75, 125, 175],
        'Close': [120, 170, 220],
        'Volume': [1000000, 2000000, 3000000],
    }
    mock_ticker = mock_yf_ticker.return_value
    mock_ticker.history.return_value = pd.DataFrame(mock_stock_data)

    # Test the get_chart function with the mock object
    symbol = 'AAPL'
    chart = get_chart(symbol)

    # Check that the mock object was called correctly
    mock_yf_ticker.assert_called_once_with(symbol)
    mock_ticker.history.assert_called_once_with(period='1y')

    # Check that the chart is not None
    assert chart is not None