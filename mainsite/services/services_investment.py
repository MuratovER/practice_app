import os

from matplotlib import pyplot as plt
from loguru import logger

def investment_calculation(stocks, deposits, portfolio):
    stock_calculation(stocks)
    portfolio_calculation(stocks, deposits, portfolio)


def portfolio_calculation(stocks, deposits, portfolio):

    profit = 0
    first_capital = 0
    full_capital = 0

    for stock in stocks:
        full_capital += float(stock.end_value)
        profit += float(stock.profit)
        first_capital += stock.invested

    portfolio.capital = "%.2f" % full_capital
    if first_capital == 0:
        portfolio_calc = 0
    else:
        portfolio_calc =( full_capital - first_capital ) / first_capital * 100

    portfolio.profit = "%.2f" % portfolio_calc
    portfolio.assets = stocks.count()+ deposits.count()
    try:
        profitability_calc = full_capital - first_capital 
    except:
        profitability_calc = 0
    portfolio.profitability = "%.2f" % profitability_calc


def stock_calculation(stocks):
    allshare = 0
    for sharestock in stocks:
        allshare += sharestock.amount
    for stock in stocks:
        stock.invested = stock.amount * stock.buy_price
        if stock.curent_price is None:
            stock.curent_price = stock.buy_price
        profit = (stock.curent_price - stock.buy_price) / stock.buy_price * 100
        stock.share = "%.2f" % ( stock.amount * 100 / allshare)
        stock.profit = "%.3f" % profit
        end_value_calc =  stock.curent_price * stock.amount
        stock.end_value = "%.2f" % end_value_calc



def chart_drawing(stocks, deposits, portfolio):

    try:
        os.remove("mainsite\static\img\chart.png")
    except:
        pass
    stock_end_value = 0
    for stock in stocks:
        stock_end_value += float(stock.end_value)



    deposit_end_value = 0

    for deposit in deposits:
        deposit_end_value += float(deposit.deposit)

    summ_assets = deposit_end_value + stock_end_value

    if stock_end_value >= deposit_end_value:
        if summ_assets != 0:
            stock_full_share = (stock_end_value * 100) / summ_assets
            deposit_full_share = 100 - stock_full_share
        else:
            stock_full_share = 0
    else:
        if summ_assets != 0:
            deposit_full_share = (deposit_end_value* 100) / summ_assets
            stock_full_share = 100 - deposit_full_share
        else:
            summ_assets = 0
    deposit_full_share = 0
    stock_full_share = 0
    plt.style.use("fivethirtyeight")

    slices = []
    labels = []
    colors = ['#FE5454', '#525AA5', '#C8CB27', '#54FEE9']
    #'#FE5454'=red, '#525AA5'=purple, '#C8CB27'=yellow, '#54FEE9'=blue
    try:
        full_stock_share_float = float("%.1f" % stock_full_share)
        full_deposit_share_float = float("%.1f" % deposit_full_share)

        slices.append(full_stock_share_float)
        slices.append(full_deposit_share_float)

        labels.append('Stocks')
        labels.append('Deposit')

        plt.pie(slices, labels=labels, colors=colors,wedgeprops={'edgecolor': 'black'})
        plt.tight_layout()
        plt.savefig("mainsite\static\img\chart.png")
    except:
        plt.savefig("mainsite\static\img\chart.png")


