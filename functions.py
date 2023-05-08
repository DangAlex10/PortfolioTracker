import yfinance as yf
import plotly.graph_objs as go
import json
import humanize
import random

def get_data(symbol):
    # Gneral Information of Stocks
    stock = yf.Ticker(symbol)
    data = {
        'symbol': symbol,
        'name': stock.info['longName'],
        'price': str(stock.info['regularMarketPrice']),
        'change': stock.info['regularMarketChange'],
        'percent_change': str(round(stock.info['regularMarketChangePercent'], 2)),
        'market_cap': humanize.intword(stock.info['marketCap'], format='%.2f'),
        'volume': humanize.intword(stock.info['regularMarketVolume'], format='%.2f')
    }
    return data