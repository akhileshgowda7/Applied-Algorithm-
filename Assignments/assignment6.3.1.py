def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = k = 0
    comparisons = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                comparisons = max(k+1,comparisons)
                return comparisons
            j += 1
            k += 1
            comparisons=max(k,comparisons)
        elif k > 0:
            k = 0
        else:
            j += 1
    return comparisons

D = 'akhileshgowdamandyaramesh'
P = 'mandyaramesh'

print("longest length of prefix: ",find_kmp(D,P))