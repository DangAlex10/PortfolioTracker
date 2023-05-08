import pytest
from unittest.mock import MagicMock
import yfinance as yf
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
def mock_yfinance(mocker):
    mock_ticker = mocker.MagicMock(spec=yf.Ticker)
    mock_info = mocker.PropertyMock(return_value={'longName': 'Mock Company'})
    type(mock_ticker).info = mock_info
    mocker.patch('yfinance.Ticker', return_value=mock_ticker)
    return mock_ticker

def test_get_chart(mock_yfinance):
    chart = get_chart('AAPL')
    assert chart.title == 'Mock Company Stock Chart'