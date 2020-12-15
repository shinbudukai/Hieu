#Name: Hieu Dang
#Date: 25 October 2020
#Project: Recursion with Sieve of Eratosthenes



def mask_index(lst, start, step):
    #create a list with entire None value
    for i in range(start, len(lst), step):  #lst = list
        lst[i] = None

def SoE(maximum):
    # create list
    prime = list(range(maximum))
    # because we start at 2
    prime[0] = None
    prime[1] = None
    for p in prime:
        if p is not None:
            #Recursive call
            mask_index(prime, 2*p, p)
    return [p for p in prime if p is not None]

def Main():
    choice = int(input("What is the range of number: "))
    print(SoE(choice))
if __name__ == "__main__":
    Main()

