def binarySearch(data,target,low,high):
    if low>high:
        return False
    else:
        mid = (low + high)//2
    if target==data[mid]:
        return True
    elif target<data[mid]:
        return binarySearch(data,target,low,mid-1)
    else:
        return binarySearch(data,target,mid+1,high)

def func(target,a,b,c):
    c.sort()
    for i in a:
        for j in b:
            total = target - i -j
            if binarySearch(c,total,0,len(c)-1):
                return True
    return False

a = [1,2,3,4,5,6,7,8,9]
b = [50,60,70,80,90]
c = [0,5,10,15,20]
print(func(100,a,b,c))