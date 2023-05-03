
import json
import time
import yahoo_fin.stock_info as si
import pandas as pd
from datetime import date
from yahoo_fin.options import *
import threading

companies_list_size = 0

#list that stores the names of companies that the user is tracking data of
companies_list = []

today = date.today()
fixdate = today.strftime("&m/%d/%y")
stock_data = {}


#function gets data of the company user is requesting
def get_stockinfo(company):
    #gets live price of company
    stock_live_price = si.get_live_price(company)
   
    #adds live price of stock to dictionary 
    stock_data[company] = stock_live_price

    #add company name to list
    companies_list[companies_list_size] = company
    companies_list_size = companies_list_size + 1



#function updates the price of the stock 
# without this function, the price in the dictionary will remain the same
def update_stockinfo(company):
    
    
    #loops the companies name in the list,
    #then updates the existing data for the company,
    #after deleting, adds new item "comapany : live stock price"
    
    for x in companies_list:
        del stock_data[x]
        stock_data.update({x:si.get_live_price(company)})



#sets an timer so update_stockinfo runs every second so the user gets live stock price 
delay = 1
start_time = threading.Timer(1,update_stockinfo)
start_time.start()



# returns the calls and put options of a company
def get_stock_options(company):
    get_options_chain(company)