

import datetime
import time

timeNow = datetime.datetime.now()
format = '%Y/%m/%d %I:%M:%p'
fixed_time = datetime.datetime.strptime(str(timeNow), '%Y-%m-%d %H:%M:%S.%f')
#Timer:
def count(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r\t')
        time.sleep(1)
        t -= 1
    print("\n---> TIME'S UP ")
#menu
def mainLoop():
    while True:
        option = input("\nChoose one option (What time is it ?/Timer? Or Enter to skip):\n- ")
    #What time is it ?
        if option == "what time is it" or option == "what time is it ?" or option == "What time is it ?" or option == "What time is it":   
            print("---->",fixed_time.strftime(format))        
        elif option == "Timer" or option == "timer":
            your_choose = input("Enter the time you want in the seconds: ")
            count(int(your_choose))
        else:
            break

if __name__ == "__main__":
    mainLoop()
