# Algorithm-1 Heap Sort Algorithm
def heapSort(d):
    input_length = len(d) - 1
    build_max_heap(d,input_length)
    for i in range(input_length,0,-1):
        d[0],d[i]=d[i],d[0]
        input_length=input_length-1
        max_heapify(d,0,input_length)
    return d

#Algorithm-2 max_heapify algorithm

def max_heapify(d,i,input_length):
    largest=i
    l=2*i+1
    r=2*i + 2

    if l<=input_length and d[l]>d[i]:
        largest=l
    else:
        largest=i
    if r<=input_length and d[r]>d[largest]:
        largest=r
    if largest !=i :
        d[i],d[largest]=d[largest],d[i]
        max_heapify(d,largest,input_length)

    return d

def build_max_heap(d,input_length):
    for i in range(((input_length)//2),-1,-1):
        max_heapify(d,i,input_length)
    return d


B=heapSort([7,5,3,7,3,7,5,4])
# A=heapSort([3,7,5,4])
A=heapSort([3,5,7,4])

print(A)
print(B)

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

def Check(A,B):
    low=0
    i=0
    flag=0
    for i in A:
        if(binarysearch(B,i,low,len(B)-1))==False:
            flag=1

    for j in B:
        if (binarysearch(A, j, low,len(A)-1)) == False:
            flag = 1

    if flag==1:
        print("The List does not contain the same set")
    else:
        print("Both the list contains the same set of elements")


Check(A,B)
