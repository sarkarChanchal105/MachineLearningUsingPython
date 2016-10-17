# from networkx.algorithms.flow.mincost import min_cost_flow
#
# #stock_prices_yesterday = [10, 7, 5, 8,4,4, 11, 9]
# #stock_prices_yesterday = [10, 10, 10, 10,10,10, 10, 10]
# stock_prices_yesterday = [10, 9,8,7,6,5,4,3,2,1]
def get_max_profit(stock_prices_yesterday):

    min_price=stock_prices_yesterday[0]
    max_profit=0

    for currrent_price in stock_prices_yesterday:
        min_price=min(min_price,currrent_price)

        pot_profit= currrent_price - min_price
        max_profit=max(max_profit,pot_profit)

    print(max_profit)

#get_max_profit(stock_prices_yesterday)


