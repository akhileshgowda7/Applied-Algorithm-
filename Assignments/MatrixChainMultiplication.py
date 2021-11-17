# Dynamic Matrix multiplication program

def RecursiveMatrixChain(p,i,j):
    if i==j:
        return 0
    values=[]
    for k in range(i,j):
        temp=(RecursiveMatrixChain(p,i,k)+RecursiveMatrixChain(p,k+1,j)+p[i-1]*p[k]*p[j])
        values.append(temp)

    minValue=min(values)
    return minValue

i=1
p=[30,35,15,5,10,20,25]
j=len(p)-1

print("Minimum number of Multiplication required is",RecursiveMatrixChain(p,i,j))


