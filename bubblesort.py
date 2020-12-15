
#import
import random
import time

#time
#def
#bubble sort
def bubble_sort(my_list):
    start_time = time.time()
    print(f'''\noriginal list--->{my_list}''')
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j+1]:
                # Swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    end_time = time.time()
    bubble_time = end_time - start_time
    print(f'''\nBubble sort --->{my_list}\n\nSpent:{bubble_time} seconds''')

#mainExe
def bubble():
    my_list = []
    number = input("\nWhat is the range of number?: ")
    try:
        for n in range(int(number)):
            my_list.append(random.randint(-100,100))
            
    #function
        bubble_sort(my_list)
    except:
        print("\n***Invalid input...***")    
if __name__ == "__main__":
    bubble()
