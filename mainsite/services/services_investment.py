def stock_calculation(stocks):
    allshare = 0
    for sharestock in stocks:
        allshare += sharestock.amount
    for stock in stocks:
        stock.invested = stock.amount * stock.buy_price
        if stock.curent_price is None:
            stock.curent_price = stock.buy_price
        profit = (stock.buy_price - stock.curent_price) / stock.buy_price
        stock.share = "%.2f" % ( stock.amount * 100 / allshare)
        stock.profit = "%.3f" % profit
        stock.end_value = stock.curent_price * stock.amount

