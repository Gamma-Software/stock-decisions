def make_trades(starting_cash, prices, crossovers):

    value = [starting_cash] #set value to starting_cash
    value = []  # creating empty set?
    stock_at = 0
    cash = starting_cash

    for i in range(0,len(prices)):
        added_value = (prices[i] - prices[i-1])/prices[i-1]
        try:
            time_index = crossovers[0][0]
            buy_index = crossovers[0][1]              
            if i == time_index:            
                if buy_index == 1:
                    stock_at = cash
                    cash = 0 
                    value.append(stock_at)                                                           
                    crossovers = crossovers[1:]
                else:
                    if(stock_at == 0):
                        cash = value[i-1]
                        value.append(value[i-1])
                    else:
                        cash = value[i-1] + value[i-1]*added_value
                        stock_at = 0
                        value.append(cash)
                    crossovers = crossovers[1:]
            else:
                if cash == 0:                
                    stock_at = value[i-1] + value[i-1]*added_value
                    value.append(stock_at)
                else:
                    value.append(cash)                      
        except (IndexError):
            added_value = (prices[i] - prices[i-1])/prices[i-1]
            if cash == 0:
                stock_at = value[i-1] + value[i-1]*added_value
                value.append(stock_at)
            else:
                value.append(cash)            
    return [round(i, 2) for i in value]
