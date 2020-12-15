#randomFactor(10000, 1000000)

#Name: Hieu Dang
#Date: 09/21/2020

import time
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
        size = input("\nHow many elements in the stack you want?: ")     
        while True:
            print(f'''\n(Enter to skip)''')
            choice = input("What you want to do with the stack (push, pop, peek, check, size)?: ")
            if choice == 'push':
                currentPtr += 1
                num = int(input("What number do you want to add?: "))
                if len(self.items) == int(size):
                    print("***Exceeding stack size***\n***Ending...")
                    sys.exit()
                self.push(num)
                print(self.items)
            if choice == 'pop':
                self.pop()
                currentPtr -= 1
                print(self.items)
            if choice == 'peek':
                print(s.peek())
            if choice == "size":
                self.size()
            if choice == 'check':
                self.checkTheLimit()
            elif choice == '':
                print("\nBacking Stack & Queue Menu...")
                time.sleep(1)
                break 

#call the stack function:
if __name__ == '__main__':
    s = Stack()
    s.process()
