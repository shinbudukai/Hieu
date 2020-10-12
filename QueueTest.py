#randomFactor(10000, 1000000)

#Name: Hieu Dang
#Date: 09/21/2020

#define the Queue
class Queue:
    def __init__(self):
        self.items = []
    def enQueue(self, item):
        self.items.insert(0, item)
    def deQueue(self):
        self.items.pop()
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
            choice = input("What you want to do with the stack (enqueue, dequeue, peek, check, size)?: ")
            if choice == 'enqueue':
                currentPtr += 1
                num = int(input("What number do you want to add?: "))
                if len(self.items) == size:
                    print("***Exceeding stack size***\n***Ending...")
                    sys.exit()
                s.enQueue(num)
                print(self.items)
            if choice == 'dequeue':
                s.deQueue()
                currentPtr -= 1
                print(self.items)
            if choice == 'peek':
                print(s.peek())
            if choice == "size":
                s.size()
            if choice == 'check':
                s.checkTheLimit()


#call the Queue function:
q = Queue()
q.process()
