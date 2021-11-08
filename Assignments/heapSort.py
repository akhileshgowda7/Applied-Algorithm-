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

print(heapSort([10,16,5,8,14,9,0,1,18]))

