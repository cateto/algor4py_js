def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val
    return x
x = [1,0,100,59,84,61]
print(x)
print(insertionSort(x))