import random
import timeit
import matplotlib.pyplot as plt


def average1(S):
    #S:sequence
    n = len(S)
    my_average = [0]*n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
            my_average[j] = total / (j+1)
            return my_average
def average2(S):
    #S:sequence
    n = len(S)
    my_average= [0]*n
    for j in range(n):
        my_average[j] = sum(S[0:j+1]) / (j+1)
        return my_average

def average3(S):
    #S:sequence
    n = len(S)
    my_average = [0]*n
    total = 0
    for j in range(n):
        total += S[j]
        my_average[j] = total / (j+1)
        return my_average

n=1
l=[]

while(n<=5000):
    rand=random.sample(range(5000),n)
    l.append(len(rand))
    n=n+1

    if __name__=="__main__":


        start = timeit.timeit()
        average1(rand)
        end = timeit.timeit()
        time_1=end-start

        start = timeit.timeit()
        average2(rand)
        end = timeit.timeit()
        time_2=end-start

        start = timeit.timeit()
        average3(rand)
        end = timeit.timeit()
        time_3=end-start

# plotting the graph

plt.plot(l,time_1,label='Average')
plt.plot(l,time_2,label='Average')
plt.plot(l,time_3,label='Average')
plt.title('Graph')
plt.xlabel('input')
plt.ylabel('Run Time')

plt.show()

