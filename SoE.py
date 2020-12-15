#Name: Hieu Dang
#Date: 25 October 2020
#Project: Sieve of Eratosthenes

#imports
from StackTest import Stack
from Queuetest1 import Queue
s = Stack()
q = Queue()

def SoE(n):
    #inialize a list with a true index
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    #We start at 2
    p = 2
    my_list = []
    while p*p <=n:
        if prime[p] == True:
            #True: 1; False:0
            #1,1,1,1,1,1,1,...
            #2,3,4,5,6,7,8,...
            #p will jump p step
            for i in range(2*p, n+1, p):
                #if n = 100
                #then create a list from 4 to 100, then counting up 2 increment
                prime[i] = False #now i = 4, so cross out 4
        p += 1 #so p now is 3, and so on until p*p <= n
    #Print out prime number
    for p in range(n+1):
        if prime[p]:
            my_list.append(p)
            s.push(p)
            q.enqueue(p)
    print("\nPrime numbers:",my_list)

def MainExe():
    numbers = int(input("What is the range of numbers?: "))
    SoE(numbers)
    print("\nStack:",s.items)
    print("\nQueue:", q.items)
if __name__ == "__main__":
    MainExe()
