def merge(A, B):
  A = [1,7,]
  B = []
  A.sort()
  B.sort()
  res = []
  i = 0
  j = 0
  while (i < len(A) and j < len(B)):
    if (A[i] >= B[j]):
      res.append(B[j])
      j = j + 1
    elif (A[i] < B[j]):
      res.append(A[i])
      i = i + 1
  if (i >= len(A)):
    for n in range(j, len(B)):
      res.append(B[n])
  if (j >= len(B)):
    for m in range(i, len(A)):
      res.append(A[m])
  print(A)
  print(B)

  return res


merge([1,7,9,7,6],[])