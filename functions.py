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

def get_chart(symbol):
    # Graphing of the stock's data
    stock = yf.Ticker(symbol)
    stock_data = yf.Ticker(symbol)
    hist = stock_data.history(period='1y')
    
    candlestick = go.Candlestick(x=hist.index,
                                 open=hist['Open'],
                                 high=hist['High'],
                                 low=hist['Low'],
                                 close=hist['Close'],
                                 name='Candlestick')
    
    line = go.Scatter(x=hist.index, y=hist['Close'], mode='lines+markers', name='Closing Price', line={'color': 'rgb(61, 89, 180)'} )
    
    fig = go.Figure(data=[candlestick, line])
    
    fig.update_layout(
        title=stock.info['longName'] + " Stock Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        font=dict(family="Helvetica, sans-serif", color="#fff"),
        paper_bgcolor="#2a2a2a",
        plot_bgcolor="#2a2a2a",
        xaxis=dict(gridcolor="#777"),
        yaxis=dict(gridcolor="#777"),
        hovermode="x",
        hoverlabel=dict(bgcolor="#444", font=dict(family="Helvetica, sans-serif", color="#fff"))

        
    )

    chart_data = json.loads(fig.to_json())
    chart = json.dumps(chart_data)
    return chart