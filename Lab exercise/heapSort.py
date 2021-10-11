def insertion(S,e):
    #s:sequence, e : element
    #step 1
    S.append(e)
    i=len(S)-1
    print(i)
    #recursive compare
    swift_up(S,i)


def swift_up(S,i):
    #base condition:hit root
    if i==0:
        print(S)
        return S
    #compare with parent
    if S[i] > S[i//2]:
        S[i],S[i//2]=S[i//2],S[i]
        # print(S)
        swift_up(S,i//2)
    else:
        return -1


if __name__=="__main__":

    print(insertion([11,7,8],15))
