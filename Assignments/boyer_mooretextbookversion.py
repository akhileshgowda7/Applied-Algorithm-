def find_boyer_moore(T, P):
    #     Return the lowest index of T at which substring P begins (or else -1).
    n, m = len(T), len(P)
    #     trivial search for empty string
    if m == 0:
        return 0
    # build ’last’ dictionary
    last = {}

    for k in range(m):
        last[P[k]] = k  # later occurrence overwrites

    i = m - 1
    k = m - 1

    while i < n:
        if T[i] == P[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text
            else:
                i -= 1  # examine previous character
                k -= 1  # ofbothTandP
        else:
            j = last.get(T[i], -1)  # last(T[i]) is -1 if not found
            #             print(k)
            #             print(j+1)
            i += m - min(k, j + 1)  # case analysis for jump step
            k = m - 1  # restart at end of pattern
    return -1



T='abacaabaccabacabaabb'
P='abacab'
print(find_boyer_moore(T,P))