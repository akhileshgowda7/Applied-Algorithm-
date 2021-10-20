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

print(insertion([1,4,3,7,6,5]))