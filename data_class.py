# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:48:36 2021

@author: Home-PC
"""

from dateutil import parser


class data_reader():
    def __init__(self, fname, use_cols = (0,1), sep = ','):
        self.use_cols = use_cols
        self.fname = fname
        self.date = []
        self.price = []
        self.sep = sep
        self.read_file()
        pass

    def read_file(self):
        file = open(self.fname, 'r', encoding = 'utf-8')
        for line in file:
            if 'dat' not in line.lower() and '\"' not in line:
                content = line.split(self.sep) #grazinamas list obejkas
                date_str = content[self.use_cols[0]]
                price_str = content[self.use_cols[1]]
                price_f = float(price_str.replace(",", "."))
                date = parser.parse(date_str).date()
                self.date.append(date)
                self.price.append(price_f)
    
    def get_year(self, year):
        dates = []
        prices = []
        for date in self.date:
            if date.year == year:
                dates.append(date)
                idx = self.date.index(date)
                price = self.price[idx]
                prices.append(price)
        return dates, prices
    
    def get_month(self, year, month, mc = 1):
        dates = []
        prices = []
        for date in self.date:
            if date.year == year:
                if date.month >= month and date.month <= (month + mc -1):
                    dates.append(date)
                    idx = self.date.index(date)
                    price = self.price[idx]
                    prices.append(price)
        return dates, prices
        
        
        
     
    
    
    
    
    
    