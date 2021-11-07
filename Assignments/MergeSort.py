def merge(A, B):
  s = []
  i = 0
  j = 0
  len_s=len(A)-1+len(B)-1
  print(s)


  while i+j<len_s:
      if j==len(B) or (i<len(A)-1 and A[i]<B[j]):
          s[i+j]=A[i]
          i=i+1
      else:
          s[i+j]=B[j]
          j=j+1


def mergeSort(s):
    input_length=len(s)-1
    if input_length<1:
        return s
    mid=input_length//2
    s1=s[0:mid]
    s2=s[mid:input_length]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1,s2)
    print(s)
    return s

mergeSort([2,6,4,8,9,10])