#Name:Hieu Dang
#Title: Factor Of 3
#Date: 09/21/2020


#import
import random
import numpy as np
import sys
#create the factors of 3
def factor_of_3(size):
    factorOf3 = []
    f = 0
    for i in range(0, size):
        f += 3 #f is factors of 3
        factorOf3.append(f)
    #print(factorOf3)
    return factorOf3

factorOf3 = factor_of_3(1000000)

    
#take the random number and check if it were factors of 3

def randomFactor(size, maximum):
    for e in range(0, size):
        rd = np.random.randint(0, maximum)
        if rd in factorOf3:
            print(rd, ":is factor of 3")
        else:
            print(rd, ":is not factor of 3")
            
#randomFactor(10000, 1000000)

#Name: Hieu Dang
#Date: 09/21/2020

#define the Stack
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop(currentPtr - 1)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        print("The size of the stack is:", len(self.items))
    def checkTheLimit(self):
        if  len(self.items) < size:
            print("***There are:", len(self.items),"/", size,"elements in the stack***")
        elif len(self.items) == size:
            print("***The stack is full***")

    def process(self):
        global size
        global currentPtr
        currentPtr = 0
        size = int(input("How many elements in the stack you want?: "))
        while True:
            choice = input("What you want to do with the stack (push, pop, peek, check, size)?: ")
            if choice == 'push':
                currentPtr += 1
                num = int(input("What number do you want to add?: "))
                if len(self.items) == size:
                    print("***Exceeding stack size***\n***Ending...")
                    sys.exit()
                s.push(num)
                print(self.items)
            if choice == 'pop':
                s.pop()
                currentPtr -= 1
                print(self.items)
            if choice == 'peek':
                print(s.peek())
            if choice == "size":
                s.size()
            if choice == 'check':
                s.checkTheLimit()


#call the stack function:
s = Stack()
s.process()
                   
                   

    
    
