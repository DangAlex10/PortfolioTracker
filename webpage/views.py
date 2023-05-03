from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
import yfinance as yf
import plotly.graph_objs as go
import json
import humanize
import random

def index_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password1 = request.POST.get('password')

        user = authenticate(username = username, password = password1)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, "Incorrect Information")
            return redirect('login')

    return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('psw')
        passwordR = request.POST.get('psw-repeat')

        if User.objects.filter(username=email):
            messages.error(request, "Email already exists")
            return redirect('signup')
        
        if password1 == passwordR:
            myuser = User.objects.create_user(email, email, password1)
            myuser.save()
            messages.success(request, "Your account has been created")
            return redirect('login')
        else: 
            return redirect('signup')

    return render(request, 'signup.html')

def stocks_page(request):
    return render(request, 'stocks.html')

def portfolio_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    symbol = user_profile.portfolio_stocks
    company_list = []

    # Gneral Information of Stocks
    for x in symbol:
        data = get_data(x)
        chart = get_chart(x)

        company_dict = {
            'data': data,
            "chart": chart
        }
        company_list.append(company_dict)

    context = {'company_list': company_list}
    return render(request, 'portfolio.html', context)


def add_portfolio(request):
    if request.method == 'POST':
        # Retrieve the user's profile and update the 'tester' field
        user_profile = UserProfile.objects.get(user=request.user)
        symbol = request.POST.get('name')
        if symbol != "" and user_profile.portfolio_stocks.count(symbol) == 0:
             user_profile.portfolio_stocks.append(symbol)
             user_profile.save()
    return redirect('stocks/' + symbol + "/")

def remove_portfolio(request):
    if request.method == 'POST':
        # Retrieve the user's profile and update the 'tester' field
        user_profile = UserProfile.objects.get(user=request.user)
        symbol = request.POST.get('name')
        user_profile.portfolio_stocks.remove(symbol)
        user_profile.save()
    return redirect('portfolio')



def signout(request):
    logout(request)
    return render(request, 'index.html')

def get_stock_data(request, symbol):
    data = get_data(symbol)
    chart = get_chart(symbol)

    context = {'data': data, 'chart': chart}
    return render(request, 'stocks.html', context)

def get_data(symbol):
    # Gneral Information of Stocks
    stock = yf.Ticker(symbol)
    data = {
        'symbol': symbol,
        'name': stock.info['longName'],
        'price': "$" + str(stock.info['regularMarketPrice']),
        'change': stock.info['regularMarketChange'],
        'percent_change': str(round(stock.info['regularMarketChangePercent'], 2)) +"%",
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