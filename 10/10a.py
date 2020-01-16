import cmath
import numpy as np


def numberAsteroids (compNumber, b):
    wList = []
    for y in range(len(b)):
        for x in range(len(b[y])):
            if b[y, x] == '#':
                newComp = complex(x, y) - compNumber
                newPhase = cmath.phase(newComp)
                #print(x, y, compNumber, newComp, newPhase)
                if not newPhase in wList:
                    wList.append(newPhase)
                    #print ('Phase added: ' , newPhase, len(wList))
    return len(wList)

    

def read_input():
    input = open('input.txt', 'r')
    inlines = input.readlines()
    lines = []
    for line in inlines:
        lines.append(list(line.strip()))

    #print(lines)
    maxX=len(lines)
    maxY=len(lines[0])
    #print(maxX, maxY)
    b = np.array(lines)
    print (b)
    print (b[2][0])

    '''
    asteroidMap=[[8 for y in range(maxY)] for x in range(maxX)]
    asteroidMap[0][1]='Y' 
    for y in range (0, maxY):
        for x in range (0, maxX):
            asteroidMap[y][x]=lines[y][x]
            print(asteroidMap)
    '''
 #   for line in lines:
        #print (line)
  #      asteroidMap.append()

    bestX = 0
    bestY = 0
    bestPos= complex(0,0)
    maxAsteroids = 0
    compNumber = complex(0,0)
    newAsteroids = 0
    #for y, yValue in enumerate(b):
    #    for x, xValue in enumerate(b):
    #        print (x)

    for y in range(len(b)):
        for x in range(len(b[y])):
            #print (x, y)
            compNumber = complex(x, y)
            if b[y,x]=='#':
                #print ('Pot asteroid:', compNumber)
                newAsteroids = numberAsteroids(compNumber, b)
                #print('new: ', newAsteroids)
                if newAsteroids > maxAsteroids:
                    maxAsteroids = newAsteroids
            newAsteroids = 0 
    #print(maxX, maxY)
    print ('Max asteroids: ', maxAsteroids)
def run_program():
    read_input()

run_program()