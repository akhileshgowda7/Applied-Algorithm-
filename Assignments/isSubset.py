def FindingSubset():
    A = [3, 7, 11, 15, 21]
    m = 25
    length = len(A)
    sub = ([[False for i in range(m + 1)]
               for i in range(length + 1)])
    # print(subset)

    for i in range(length + 1):
        sub[i][0] = True

    for i in range(1, m + 1):
        sub[0][i] = False

    for i in range(1, length + 1):
        for j in range(1, m + 1):
            if j < A[i - 1]:
                sub[i][j] = sub[i - 1][j]
            if j >= A[i - 1]:
                sub[i][j] = (sub[i - 1][j] or
                                sub[i - 1][j - A[i - 1]])

    if(sub[length][m])==True:
        print("There exists a subset\n")
    else:
        print("The does not exists a Subset\n")

    return sub[length][m]


print(FindingSubset())


