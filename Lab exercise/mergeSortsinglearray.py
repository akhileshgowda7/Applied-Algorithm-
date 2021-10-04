def merge(A, B):
    A = [1, 4, 5, 2, 3]
    B = [6, 8, 7, 10, 0, -1]
    A.sort()
    B.sort()
    c = A + B
    res = []
    i = 0
    j = len(A)

    while (i < len(A) and j < len(c)):
        if (c[i] >= c[j]):
            res.append(c[j])
            j = j + 1
        elif (c[i] < c[j]):
            res.append(c[i])
            i = i + 1
    if (i >= len(A)):
        for n in range(j, len(c)):
            res.append(c[n])
    if (j >= len(c)):
        for m in range(i, len(A)):
            res.append(c[m])
    print(A)
    print(B)
    print(res)
    return res


merge([1, 4, 5, 2, 3], [6, 8, 7, 10, 0, -1])