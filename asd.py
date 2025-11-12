def positive_sum(arr):
    # Your code here
    list =[]
    for i in arr:
        list.append(abs(i))
    x=sum(list)
    return x
