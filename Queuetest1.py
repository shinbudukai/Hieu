#Name: Hieu Dang
#Date: 10/11/2020
import sys
import time
#define the Queue
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        self.items.pop(currentPtr - 1)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        print("The size of the Queue is:", len(self.items))
    def checkTheLimit(self):
        if  len(self.items) < size:
            print("***There are:", len(self.items),"/", size,"elements in the queue***")
        elif len(self.items) == size:
            print("***The Queue is full***")

    def process(self):
        global size
        global currentPtr
        currentPtr = 0
        size = input("How many elements in the Queue you want?: ")
        while True:
            print(f'''\n(Enter to skip)''')  
            choice = input("What you want to do with the Queue (enqueue, dequeue, peek, check, size)?: ")
            if choice == 'enqueue':
                currentPtr += 1
                num = int(input("What number do you want to add?: "))
                if len(self.items) == int(size):
                    print("***Exceeding Queue size***\n***Ending...")
                    sys.exit()
                self.enqueue(num)
                print(self.items)
            if choice == 'dequeue':
                self.dequeue()
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

#call the Queue function:
if __name__== '__main__':
    q = Queue()
    q.process()
