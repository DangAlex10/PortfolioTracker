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
    }
    return data