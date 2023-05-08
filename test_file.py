import functions
import pytest

@pytest.fixture
def mock_yf_ticker(mocker):
    mock_ticker = mocker.Mock()
    mock_ticker.info = {
        'longName': 'Apple Inc.',
        'regularMarketPrice': 138.95,
        'regularMarketChange': 0.49,
        'regularMarketChangePercent': 0.35,
        'marketCap': 234400000000,
        'regularMarketVolume': 7900000
    }
    mocker.patch('functions.yf.Ticker', return_value=mock_ticker)

def test_get_data(mock_yf_ticker):
    data = functions.get_data('AAPL')
    assert isinstance(data, dict)
    assert 'symbol' in data
    assert 'name' in data
    assert 'price' in data
    assert 'change' in data
    assert 'percent_change' in data
    assert 'market_cap' in data
    assert 'volume' in data