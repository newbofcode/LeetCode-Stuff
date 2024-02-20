def stocktrader2(list1):
    profits = 0
    for i in range(1,len(list1)):
        if list1[i] > list1[i-1]:
            profits += list1[i]-list1[i-1]
    return profits
