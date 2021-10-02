def binarysearch(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return data[mid]
        elif target<data[mid]:
            return binarysearch(data,target,low,mid-1)
        else:
            return binarysearch(data,target,mid+1,high)


print(binarysearch([1,2,3,4,5,6,7,8,9],8,1,9))