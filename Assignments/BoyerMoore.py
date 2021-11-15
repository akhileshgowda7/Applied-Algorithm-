def find_boyer_moore(T, P):
    count=0
    flag=0
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        flag+=1
        # If match, decrease i,k
        if T[i] == P[k]:
            if k == 0:
                count+=1
                i=i+flag
            else:
                i -= 1
                k -= 1
        # Not match, reset the positions
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1
    return count

occurences=find_boyer_moore('cdcdcdcdc','cdc')
print(f"non overlapping occurences  is :{occurences}")