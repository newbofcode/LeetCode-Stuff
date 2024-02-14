def stocktrader(arr1):
    profit = buy = sell = 0
    for i,v in enumerate(arr1):
        if i < len(arr1):
            for a,b in enumerate(arr1[i+1:]):
                temp = b - v
                if profit < temp:
                    profit = temp
                    buy = i+1
                    sell = a+i+2
    return profit
