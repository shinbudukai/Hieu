#Name: Hieu Dang
#Date: 10/11/2020
import sys

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
        size = int(input("How many elements in the Queue you want?: "))
        while True:
            choice = input("What you want to do with the Queue (enqueue, dequeue, peek, check, size)?: ")
            if choice == 'enqueue':
                currentPtr += 1
                num = int(input("What number do you want to add?: "))
                if len(self.items) == size:
                    print("***Exceeding Queue size***\n***Ending...")
                    sys.exit()
                s.enqueue(num)
                print(self.items)
            if choice == 'dequeue':
                s.dequeue()
                currentPtr -= 1
                print(self.items)
            if choice == 'peek':
                print(s.peek())
            if choice == "size":
                s.size()
            if choice == 'check':
                s.checkTheLimit()


#call the Queue function:
s = Queue()
s.process()
