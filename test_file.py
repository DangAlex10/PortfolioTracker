import pytest
from unittest.mock import patch
from functions import get_data

@pytest.mark.parametrize("symbol, expected_name", [
    ("AAPL", "Apple Inc."),
    ("GOOGL", "Alphabet Inc.")
])
@patch("webpage.views.yf.Ticker")
def test_get_data(mock_ticker, symbol, expected_name):
    # Create a mock Ticker object
    mock_info = {"longName": expected_name, "regularMarketPrice": 100, "regularMarketChange": 1.0, "regularMarketChangePercent": 1.0, "marketCap": 1000000000, "regularMarketVolume": 1000000}
    mock_ticker.return_value.info = mock_info

    # Call the get_data function with the given symbol
    data = get_data(symbol)

    # Check that the returned data is correct
    assert data["symbol"] == symbol
    assert data["name"] == expected_name