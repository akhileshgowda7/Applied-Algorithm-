

def MergeSort(s1,s2):
    s=[]
    i=j=0
    len_s1=len(s1)
    len_s2=len(s2)
    len_s=len_s1+len_s2
    while j<len_s2-1 and i<len_s1-1:
        if s1[i]<s2[j]:
            s.append(s1[i])
            i+=1
        else:
            s.append(s2[j])
            j+=1
    while i<len_s1:
        s.append(s1[i])
        i+=1
    while j<len_s2:
        s.append(s2[j])
        j+=1
    print(s)
    return s
s1=[2,5,8,11,12,14,15]
s2=[3,9,10,18,19,22,25]
MergeSort(s1,s2)

