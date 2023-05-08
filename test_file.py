import pytest
import json
from unittest import mock
from unittest.mock import MagicMock
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

@pytest.fixture
def mock_yf_ticker_chart():
    # Create a mock object for yf.Ticker class
    mock_ticker = mock.Mock()
    mock_ticker.info = {'longName': 'Mock Stock'}
    mock_ticker_data = mock.Mock()
    mock_ticker_data.history.return_value = {
        'Open': [100, 110, 120],
        'High': [120, 130, 140],
        'Low': [90, 100, 110],
        'Close': [110, 120, 130],
        'Date': ['2022-05-01', '2022-05-02', '2022-05-03']
    }
    mock_ticker.return_value = mock_ticker_data
    return mock_ticker


def test_get_chart(mock_yf_ticker_chart):
    # Test the get_chart function with the mock object
    symbol = 'mock'
    chart = get_chart(symbol)
    chart_data = json.loads(chart)
    candlestick_data = chart_data['data'][0]['ohlc']
    line_data = chart_data['data'][1]['y']
    
    assert chart_data['layout']['title']['text'] == 'Mock Stock Stock Chart'
    assert len(candlestick_data['open']) == 3
    assert candlestick_data['open'][0] == 100
    assert candlestick_data['high'][1] == 130
    assert line_data[2] == 130