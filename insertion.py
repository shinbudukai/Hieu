
#import
import random
import time

#time
#def
#Insertion sort
def insertion_sort(my_list):
    start_time = time.time()
    print(f'''\noriginal list--->{my_list}''')
    for i in range(1, len(my_list)):
        crtValue = my_list[i]
        crtIndex = i
        while crtIndex > 0 and my_list[crtIndex-1] > crtValue:
            my_list[crtIndex] = my_list[crtIndex-1]
            crtIndex = crtIndex - 1
        my_list[crtIndex] = crtValue
    end_time = time.time()
    insertion_time = end_time - start_time
    print(f'''\nInsertion sort --->{my_list}\n\nSpent:{insertion_time} seconds''')
#mainExe
def insertion():
    my_list = []
    number = input("\nWhat is the range of number?: ")
    try:
        for n in range(int(number)):
            my_list.append(random.randint(-100,100))
    #function
        insertion_sort(my_list)
    except:
       print("\n***Invalid input...***")   
if __name__ == "__main__":
    insertion()
