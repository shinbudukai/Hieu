#Name: Hieu Dang
#Date: 11 October 2020
#Project Name: Link Listed


import random

#Class link listed
class node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = node()
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total
    def display(self):
        my_list = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            my_list.append(cur_node.data)
            print(my_list)
    def get(self, index):
        if index >= self.length():
            print("----> The index is invalid")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                print(f"""\n---->Linked List[{cur_idx}]: {cur_node.data}""")
                return cur_node.data
            cur_idx += 1
        
def mainExe():
    #calling function
    l = linkedList()
    while True:
        your_choice = input(f'''\nType "try" to test again/Enter to skip: ''')
        if your_choice == "try":
            resulting = "Resulting..."
            print(resulting)
            #initalize my List:
            for i in range(10000):
                FirstList = []
                for i in range(5):
                    #this list contains random number
                    SecondList = []
                    for i in range(10):
                        SecondList.append(random.randint(-1000000,1000000))

                    #Search for the Max in the List
                    MAX = 0
                    for i in SecondList:
                        if MAX < i:
                            MAX = i
                    FirstList.append(MAX+1)   #plus 1 as the requirement of the problem
                    # Use linked list at this time      
                l.append(FirstList)

            #l.display()
            resulted = resulting.replace("Resulting...","Resulted")
            print(resulted)
            l.get(random.randint(0,10000))
        elif your_choice == "":
            break
if __name__ == "__main__":
    mainExe()
