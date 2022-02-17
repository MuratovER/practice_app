def investment_calculation(stocks, portfolio):
    stock_calculation(stocks)


# def portfolio_calculation(stock_obj, portfolio):
#     portfolio.assets = stock_obj.count()
#


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
        stock.end_value = stock.curent_price * stock.amount

