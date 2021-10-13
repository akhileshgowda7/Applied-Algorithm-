def countingSort(d, k):
    b = []
    c = []
    b=[0]*len(d)
    input_length = len(d)
    # print(input_length)
    # print(k)
    for i in range(0, k+1):
        c.append(0)

    for j in range(1, input_length):
        c[d[j]] = c[d[j]]+1


    for i in range(1, k+1):
        c[i] = c[i] + c[i -1]

    for j in range(input_length-1,-1,-1):
        b[c[d[j]]] = d[j]
        c[d[j]] = c[d[j]] - 1

    return b


d = [2, 5, 3, 0, 2, 3, 0, 3]
print(countingSort(d, 5))