def countingSort(d, k):
    b = []
    c = []
    b=[0]*len(d)
    input_length = len(d)-1
    c=[0]*len(d)
    # print(input_length)
    i=0
    for i in range(0, input_length):
        print(i)
        ind=d[i]//k
        c[ind % 10] = c[ind % 10]+1


    for i in range(1, input_length-1):
        c[i] = c[i] + c[i -1]

    for j in range(input_length-1,0,-1):
        ind=d[i]//k
        b[c[ind%10]-1] = d[j]
        c[ind % 10] = c[ind % 10] - 1

    return b

def Radix_Sort(d):
    mx=max(d)
    exponent=1
    while((mx/exponent)>0):
        countingSort(d,exponent)
        exponent*=10
    return d

d=[400,200,340,120,80,40,320]
Radix_Sort(d)
