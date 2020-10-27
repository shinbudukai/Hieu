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
def checkLimit():
    global currentPtr
    currentPtr += 1
    if sizeStack == currentPtr:
        print("***Exceeding size...***")
        sys.exit()


def ListrandomFactor(sizelist, maximum):
    global currentPtr
    currentPtr = 0
    for e in range(0, sizelist):
        rd = np.random.randint(0, maximum)
        if rd in factorOf3:
            print(rd," :is factor of 3")
        else:
            print(rd," :is not factor of 3")
        checkLimit()



sizeStack = int(input("What size do you want the Queue be: "))
ListrandomFactor(10, 10)
