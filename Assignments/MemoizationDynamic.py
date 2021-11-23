import sys

def MemoizedMatrixChain(p):
    n=len(p)-1
    m = [[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        for j in range(i,n):
            m[i][j]=sys.maxsize
    #print(m)
    return LookUpChain(m,p,0,n-1)

def LookUpChain(m,p,i,j):
    #print(i , j)
    if m[i][j] < sys.maxsize:
        return m[i][j]
    # print(m)
    if i == j:
        m[i][j]=0
    else:
        for k in range(i,j-1):
            q =LookUpChain(m,p,i,k)+LookUpChain(m,p,k+1,j)+ p[i-1]* p[k] * p[j]
            # print(q)
            # print(1)
            if q < m[i][j]:
                m[i][j]=q
    print(m[i][j])
    return m[i][j]

p=[30,35,15,5,10,20,25]

print(MemoizedMatrixChain(p))


