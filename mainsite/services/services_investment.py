def investment_calculation(stocks, portfolio):
    stock_calculation(stocks)
    portfolio_calculation(stocks, portfolio)


def portfolio_calculation(stocks, portfolio):

    profit = 0
    first_capital = 0
    full_capital = 0

    for stock in stocks:
        full_capital += float(stock.end_value)
        profit += float(stock.profit)
        first_capital += stock.invested

    portfolio.capital = "%.2f" % full_capital
    portfolio_calc =( full_capital - first_capital ) / first_capital * 100
    portfolio.profit = "%.2f" % portfolio_calc
    portfolio.assets = stocks.count()
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

