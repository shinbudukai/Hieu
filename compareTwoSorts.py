
#import
import random
import time

#time
#def
#bubble sort
def bubble_sort(my_list):
    
    #print(f'''\noriginal list--->{my_list}''')
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j+1]:
                # Swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

#Insertion sort
def insertion_sort(my_list):
    start_time = time.time()
    for i in range(1, len(my_list)):
        crtValue = my_list[i]
        crtIndex = i
        while crtIndex > 0 and my_list[crtIndex-1] > crtValue:
            my_list[crtIndex] = my_list[crtIndex-1]
            crtIndex = crtIndex - 1
        my_list[crtIndex] = crtValue
  

#mainExe
def mainloops():

    number = input("\nHow many number you want to compare?/Enter to exit: ")
    while True:
        resulting = "Resulting..."
        print(resulting)
        my_list = []
        if number == '':
            print("\nExiting comparision...")
            time.sleep(1)
            break
        for n in range(int(number)):
            my_list.append(random.randint(1,999))

    #function
        #bubble
        start_time1 = time.time()
        bubble_sort(my_list)
        end_time1 = time.time()
        bubble_time = end_time1 - start_time1
        #Insertion
        start_time2 = time.time()
        insertion_sort(my_list)
        end_time2 = time.time()
        inser_time = end_time2 - start_time2
        resulted = resulting.replace("Resulting...", "Resulted")
        print(resulted)
        print("----------------------------------------------------------")
        print(f'''\nNumber\tBubble Sort\t\t\tInsertion Sort''')
        if bubble_time > 0:
            result = (f'''\n{number}\t{bubble_time}(s)\t\t{inser_time}(s)''')
            print(result)
        else:
            result =(f'''\n{number}\t{bubble_time}(s)\t\t\t\t{inser_time}(s)''')
            print(result)
        number = input("\nHow many number you want to compare?/Enter to exit: ")
if __name__ == "__main__":
    mainloops()
