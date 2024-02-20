def jumpgame(list1):
    is_not_0_counter = 0
    for i,v in enumerate(list1):
        if v == 0 and is_not_0_counter == 0:
            return False
        elif v+i >= len(list1):
            return True
        elif list1[v+i] > 0:
            is_not_0_counter += 1
    return True
