import threading
import time
import sys
from inputimeout import inputimeout, TimeoutOccurred
from timeit import default_timer as timer


sys.setrecursionlimit(5000) # to skip stack overflow error
timeout = 30 # program will exit after 30 sec.
endTime = timer() + timeout
result = list()
runFlag = True


def fibonacci(number):
    if not runFlag:
        exit()
    if(number <=1):
        return number
    else:
        return(fibonacci(number - 1) + fibonacci(number -2))
    
def getInput():
    while runFlag :
        #time.sleep(0.1)
        myNum = 0
        startime = timer()
        try:
            myNum = int( inputimeout(prompt='>>',  timeout=endTime-startime))
        except TimeoutOccurred:
            print('time out')
           
        
        if((myNum == 0) or (myNum <=5000) ):
            result.append((fibonacci(myNum)))
        
        else:
            print('invalid input!.')
        
        


myThread_timer= threading.Thread(target = getInput, args=[])
myThread_timer.start()
time.sleep(timeout)
runFlag= False
print('')
myThread_timer.join()
for r in result:
    print(r)

exit()

    


    