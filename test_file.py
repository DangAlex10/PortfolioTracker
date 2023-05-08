import functions

def test_get_data():
    data = functions.get_data('AAPL')
    assert isinstance(data, dict)
    assert 'symbol' in data
    assert 'name' in data
    assert 'price' in data
    assert 'change' in data
    assert 'percent_change' in data
    assert 'market_cap' in data
    assert 'volume' in data