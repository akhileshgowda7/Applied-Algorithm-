def insertion(a):
    # print(len(a))

    for j in range(1,len(a)):
        # print(j)
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a


def BucketSort(d):
    input_length=len(d)
    b=[]
    for i in range(0,input_length):
        b.append([])

    for i in range(0,input_length):
        ind=int((input_length)*d[i])
        b[ind].append(d[i])


    for i in range(0,input_length):
        b[i]=insertion(b[i])


    s=[]
    for i in range(0,len(b)-1):
        if b[i]:
            s.append(b[i])
    return s

print(BucketSort([0.25,0.23,0.95,0.56,0.53,0.96,0.45,0.44]))
