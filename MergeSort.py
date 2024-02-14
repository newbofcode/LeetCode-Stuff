def mergesort(list1):
    #base case
    if len(list1) <= 1:
        return list1
    #variables
    a=b=0
    list_center = len(list1)//2
    sorted_list = []
    left_merge = mergesort(list1[:list_center])
    right_merge = mergesort(list1[list_center:])
    #sorting
    stop = False
    while not stop:
        if a < len(left_merge) and b < len(right_merge):
            if left_merge[a] <= right_merge[b]:
                sorted_list.append(left_merge[a])
                a+=1
            elif left_merge[a] > right_merge[b]:
                sorted_list.append(right_merge[b])
                b+=1
        elif a == len(left_merge):
            sorted_list.extend(right_merge[b:])
            return sorted_list
        elif b == len(right_merge):
            sorted_list.extend(left_merge[a:])
            return sorted_list
