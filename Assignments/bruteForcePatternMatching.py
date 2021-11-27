def find_brute(T,P):
    n,m=len(T),len(P)
    # every starting position
    for i in range(n - m + 1):
        k = 0
    # conduct O(k) comparisons while k < m and T[i+k] == P[k]:
        k += 1
        if k == m:
            return i
    return -1

print(find_brute('cdcdcdcdc','cdc'))