def majority(list1):
    counter_dict = {}
    key = None
    value = 0
    for i in list1:
        if i in counter_dict:
            counter_dict[i]+=1
            if counter_dict[i] > value:
                value = counter_dict[i]
                key = i
        else:
            counter_dict[i] = 1
    return key
