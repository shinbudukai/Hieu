#Name: Hieu Dang
#Project Name: Menu
#Date: 20 October 2020

#import
import os
import time
from Timer import*
from factorOf3 import*
from StackTest import*
from Queuetest1 import*
from LinkedList import*
from SoE import*
from RecursionSoE import*
from bubblesort import*
from insertion import*
from compareTwoSorts import*
#color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    RED = '\033[31m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#define
def clr():
    os.system('cls')
def menu(file):
    file = open(file, 'r')
    theList = file.readlines()
    file.close()
    for i in range(len(theList)):
        theList[i] = theList[i].replace("\n","")

    for i in range(2, len(theList)):
        print(theList[i])
    return
def innerPage(name):
    print("Project Name: Main Menu\t\t\t\t\t\t  By: Hieu Dang\nScreen Name:",name," \t\t\t  Date: October 20 2020\n\n\t\t\t\t",name)
    return
def back():
    backs = input("\n\n\n\nEnter to get back...")
#main loop
clr()
print(f'''{bcolors.OKGREEN}{bcolors.BOLD}\n\n\n\t\t\t***WELCOME TO HIEU DANG MENU...***{bcolors.ENDC}''')
time.sleep(2)
while True:
    clr()
    MainM = menu("Main menu.txt")
    option = input("Please make your option(1,2,3,4,5,6,7): ")
    if option == "1":
        clr()
        innerPage("Project1:Timer\t")
        mainLoop()
        back()
    elif option == "2":
        clr()
        innerPage("Project2:Factor Of 3")
        mainExec()
        back()        
    elif option == "3":
        while True:
            clr()
            SandQ = menu("stack&queue.txt")
            option3 = input("Please make your option(1,2,3): ")
            if option3== "1":
                clr()
                innerPage("Stack\t\t")
                s = Stack()
                s.process()
            elif option3 == "2":
                clr()
                innerPage("Queue\t\t")
                q = Queue()
                q.process()
            elif option3 == "3":
                break
            else:
                print(f"""{bcolors.RED}{bcolors.BOLD}\n\t\t\t***ERROR: No option choosen***{bcolors.ENDC}""")
                time.sleep(1)
    elif option == "4":
        clr()
        innerPage("Project4:Linked List")
        mainExe()
        back()
    elif option == "5":
        while True:
            clr()
            Soe = menu("Soe.txt")
            option5 = input("\nPlease make your option(1,2,3): ")
            if option5 == "1":
                clr()
                innerPage("Prime numbers with SoE")
                MainExe()
                back()
            elif option5 == "2":
                clr()
                innerPage("Recursion with Soe")
                Main()
                back()
            elif option5 == "3":
                break
            else:
                print(f"""{bcolors.RED}{bcolors.BOLD}\n\t\t\t***ERROR: No option choosen***{bcolors.ENDC}""")
                time.sleep(1)
    elif option == "6":
        while True:
            clr()
            sort = menu("sortingA.txt")
            option6 = input("\nPlease make your option(1,2,3,4): ")
            if option6 == "1":
                clr()
                innerPage("Bubble sort\t")
                bubble()
                back()
            elif option6 == "2":
                clr()
                innerPage("Insertion sort\t")
                insertion()
                back()
            elif option6 == "3":
                clr()
                innerPage("Compare two sorts")
                mainloops()
                back()
            elif option6 == "4":
                break
            else:
                print(f"""{bcolors.RED}{bcolors.BOLD}\n\t\t\t***ERROR: No option choosen***{bcolors.ENDC}""")
                time.sleep(1)
    elif option == "7":
        clr()
        print(f'''{bcolors.OKGREEN}{bcolors.BOLD}\n\n\n\t\t\t***EXITING MAIN MENU...***{bcolors.ENDC}''')
        time.sleep(1)
        clr()
        break
    else:
        print(f"""{bcolors.RED}{bcolors.BOLD}\n\t\t\t***ERROR: No option choosen***{bcolors.ENDC}""")
        time.sleep(1)

