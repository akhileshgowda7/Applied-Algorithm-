import sys
def PrintOptimalParents(s,i,j):
    if i==j:
        print('A' +str(i), end="")
    else:
        print("(",end="")
        PrintOptimalParents(s,i,s[i][j])
        PrintOptimalParents(s,s[i][j]+1,j)
        print(")",end="")


def MatrixChainOrder(p):
    n=len(p)

    # m=[[0]*n]*n
    # s=[[0]*n]*n

    m = [[0 for x in range(n)]for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for i in range(1,n):
        m[i][i]=0

    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j] = sys.maxsize
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                print(q)
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    PrintOptimalParents(s,i,j)
    return m, s

p=[30,35,15,5,10,20,25]
i=1
j=len(p)-1
m,s=MatrixChainOrder(p)
print("\nMinimum number of Multiplication required is",m[i][j] )


