# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:45:09 2021

@author: Home-PC
"""

#                           # 06 lesson

from data_class import data_reader  # calling class with methods for reading data from files
import matplotlib.pyplot as plt


brent = data_reader("BrentOilPrices.csv")
rubusd = data_reader("RUB_USD.dat", sep='\t', use_cols=(1, 2))

common_dates = []
brent_prices = []
rub_prices = []


def extract_same_region():
    for date in brent.date:
        if date in rubusd.date:
            common_dates.append(date)
            idx_rub = rubusd.date.index(date)
            rub_price = rubusd.price[idx_rub]
            rub_prices.append(rub_price)
            idx_brent = brent.date.index(date)
            brent_price = brent.price[idx_brent]
            brent_prices.append(brent_price)


extract_same_region() 
y = 2017    # selected year for plotting
m = 3       # selected month for plotting
mc = 4      # selected month count for plotting

brent_d2001, brent_p2001 = brent.get_year(y)
rub_d2001, rub_p2001 = rubusd.get_year(y)

brent_dmm, brent_pmm = brent.get_month(y, m, mc)
rub_dmm, rub_pmm = rubusd.get_month(y, m, mc)
            
fig, (plotB, plotC, plotD) = plt.subplots(3, 1)

plotB.plot(common_dates, brent_prices, label="Brent")
plotB.plot(common_dates, rub_prices, label="RUB_USD")
plotB.legend()
plotB.set_title("All times")

plotC.plot(brent_d2001, brent_p2001, label="Brent")
plotC.plot(rub_d2001, rub_p2001, label="RUB_USD")
plotC.legend()
plotC.set_title("Selected year: " + str(y))

plotD.plot(brent_dmm, brent_pmm, label="Brent", marker='o')
plotD.plot(rub_dmm, rub_pmm, label="RUB_USD", marker="o")
plotD.set_title("Selected " + str(mc) + " months, starting " + str(y) + "-" + str(m))
plotD.legend()

fig.tight_layout()
plt.show()
