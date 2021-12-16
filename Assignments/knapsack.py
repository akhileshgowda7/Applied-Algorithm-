def KnapSack(Input_list,s):

    m = [[0 for i in range(s+1)] for j in Input_list]
    for i in range(len(Input_list)):
        for j in range(s+1):
            if j==0:
                m[i][j]=1
            if i==0 and j>0:
                if Input_list[i]==j:
                    m[i][j]=1
                else:
                    m[i][j]=0
            elif(j<Input_list[i] and j>0):
                m[i][j]=m[i-1][j]
            elif(j>0):
                m[i][j]=m[i-1][j-Input_list[i]]
            if m[i-1][j]==1:
                m[i][j]=1

    subset=[]
    j=s
    i=len(Input_list)-1
    while j>=0:
        if(m[i][j]==1 and m[i-1][j]==1):
            i=i-1
        if(m[i][j]==1 and m[i-1][j]==0):
            j=j-Input_list[i]
            subset.append(Input_list[i])
            i=i-1
        if i==0:
            subset.append(j)
            break

    sum = 0

    for i in subset:
        sum+=i

    return sum,subset


Input_list= [5, 23, 27, 37, 48, 51, 63, 67, 71, 75, 70, 83, 889, 91, 101, 112, 121, 132, 137, 141, 143, 147, 153, 159, 171, 181, 190, 191]
s=762
print(KnapSack(Input_list,s))

