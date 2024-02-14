def rotateArray(arr1,rotate):
    temp = arr1[0]
    index = 0
    counter = 0
    while counter < len(arr1):
        index = (index + rotate)%len(arr1)
        arr1[index], temp = temp, arr1[index]
        counter += 1
        if counter%2==0 and len(arr1)%2 == 0:
            index = (index + 1)%len(arr1)
            temp = arr1[index]
    return arr1
