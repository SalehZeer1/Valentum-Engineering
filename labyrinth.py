import sys
import pprint

sys.setrecursionlimit(27000) # to skip stack overflow error

##################################################
###### Finding path  S-> E 
##################################################

def searchHome(deepL,  coloC,  rawR):
    if((deepL == endL) and (coloC == endC) and (rawR == endR)):
        return True  #you are at home
    if ((labyrinth[deepL][coloC][rawR] == '#') or (visitedCells[deepL][coloC][rawR] == 'x')):
        dicPath()
        return False #you are in the wall or in visited cell 
    visitedCells[deepL][coloC][rawR] = 'x'
  
    if(rawR >0):
        incPath()
        if(searchHome(deepL,coloC,rawR-1)):
            correctPath[deepL][coloC][rawR]= 'y'
            return True
    if(rawR < r-1):
        incPath()
        if(searchHome(deepL,coloC,rawR +1)):
            correctPath[deepL][coloC][rawR]= 'y'
            return True
        
    if(coloC >0):
        incPath()
        if(searchHome(deepL,coloC -1,rawR)):
            correctPath[deepL][coloC][rawR]= 'y'
            return True
    if(coloC < c-1):
        incPath()
        if(searchHome(deepL,coloC +1,rawR)):
            correctPath[deepL][coloC][rawR]= 'y'
            return True
        
    if(deepL >0):
        incPath()
        if (searchHome(deepL -1 , coloC , rawR)):
            correctPath[deepL][coloC][rawR]= 'y'
            return True
    if(deepL < l-1):
        incPath()  
        if(searchHome(deepL + 1, coloC, rawR)):   
            correctPath[deepL][coloC][rawR]= 'y'
            return True
        
    return False


#######################################################
########## to calculate the shortest visited path
#########################################################
path = 0
def incPath():
    global path
    path +=1

def dicPath():
    global path
    path -=1
    
####################################
###### def constants:
####################################
startL, startC, startR = 0,0,0  # Start point address
endL, endC,endR = 0,0,0 # End Point address


##################################################
######## processing  the input
##################################################

while True:
    path =0 # reset path
    print('please, enter the dimension of the labyrinth!')
    l,c,r = list(map(int, input().split()))   # input labyrinth dimensions
    if ((l > 30) or (c > 30) or (r > 30)):
        print('the labyrinth is too big, values must be < 30')
        continue
    if ((l == 0) and (c == 0) and (r == 0)):
        exit()
    labyrinth = [[[0 for col in range(r)]for row in range(c)] for x in range(l)]
    #intitial labyrinth dimensions:
    for z in range(l):
        for y in range(c):
            raw = input()
            for x in range(r):
                labyrinth[z][y][x] = raw[x]
                if(raw[x] == 'S'):
                    startL =z
                    startR=x
                    startC=y
                elif(raw[x] == 'E'):
                    endL= z
                    endC=y
                    endR = x
                elif (raw[x] == '.' or raw[x] == '#'):
                    continue
                else:
                    print('invalid input')
                    exit()
                
        print()     


#TO DO: check the inputs (are all cells filled correctly?)


    visitedCells = [[[0 for col in range(r)]for row in range(c)] for deep in range(l)]
    correctPath = [[[0 for col in range(r)]for row in range(c)] for deep in range(l)]


    for deep in range(l):
        for colomn in range(c):
            for raw in range(r):
                visitedCells[deep][colomn][raw] = 'n' #not visited cells
                correctPath[deep][colomn][raw] = 'n'    # not correctpath


    solution = searchHome(startL, startC, startR)
    if (solution):
        print('Entkommen in ' + str(path) + ' Minute(n)!')
    else:
        print('Gefangen :-(')
