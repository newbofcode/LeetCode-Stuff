def removeE(list1,element):
    a=b=c=0
    while a < len(list1) and b < len(list1):
        if list1[a] == element or list1[a] == '_':
            b+=1
            if b == len(list1):
                list1[b-1] = '_'
                break
            if list1[b] == element or list1[b] == '_':
                list1[b] = '_'
                b+=1
            else:
                list1[a] = list1[b]
                list1[b] = '_'
                a+=1
                c+=1
        else:
            a+=1
            b=a
            c+=1
    return f"{c}, nums = {list1}"