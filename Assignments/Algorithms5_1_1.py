# Brute force
def find_brute(T, P):
    count=0
    n, m = len(T), len(P)
    i=0
    while(i<n-m+1):
        k = 0
        while k<m and T[i+k] == P[k]:
            k += 1
        if k == m:
            count+=1
            i=i+m
        else:
            i=i+1
    return count


occurences=find_brute('cdcdcdcdc','cdc')
if occurences==0:
    print("Pattern not found")
else:
    print("non overlapping occurences is:",occurences)

# #  Boyer - Moore
# def find_boyer_more(T , P ):
#     count = 0
#     n , m = len(T) , len (P)
#     if m == 0:
#         return 0
#     last = {}
#     for k in range ( m ) :
#         last [P[k]] = k
#     i = m -1
#     k = m -1
#     while i < n :
#         if T [i] == P[k]:
#             if k == 0:
#                 count += 1
#                 i += 2 * (m - 1) + 1
#             else :
#                 i -= 1
#                 k -= 1
#         # Not match , reset the positions
#         else :
#             j = last.get(T[i], -1)
#             i += m - min (k , j + 1)
#             k = m -1
#     return count
#
# # KMP failure function
# def compute_kmp_fail (P) :
#     m = len(P)
#     fail = [0] * m
#     j = 1
#     k = 0
#     while j < m :
#         if P [ j ] == P [ k ]:
#             fail [j] = k+1
#             j += 1
#             k += 1
#         elif k > 0:
#             k = fail [k -1]
#         else :
#             j += 1
#     return fail
#
# # KMP
# def find_kmp(T,P):
#     count = 0
#     n , m = len( T ) , len ( P )
#     if m == 0:
#         return 0
#     fail = compute_kmp_fail ( P )
#     j = 0
#     k = 0
#     while j < n :
#         if T [j] == P[k]:
#             if k == m-1:
#                 count += 1
#                 k = -1
#             j += 1
#             k += 1
#         elif k > 0:
#             k = fail [k -1]
#         else :
#             j += 1
#     return count
#
# text_patt = [("abcaabcaabcaabca", "abca"), ("b" * 10, "bb"), ("aaaaabaaaaaa", "ba"),\
#              ("aaaaaaaaaaaaa", "b")]
# for D, P in text_patt:
#     # print(f"{P} occurs {find_brute(D, P)} times in D: {D}, while using Brute Force Algorithm ")
#     # print(f" {P} occurs {find_boyer_more(D, P)} times in D: {D}, while using  Boyer Moore Algorithm")
#     print(f"{P} occurs {find_kmp(D, P)} times in D: {D},while using KMP failure Function")