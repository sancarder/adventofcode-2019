def getWire():
    line = input.readline().strip()
    return line.split(',') 

def getSteps(step):
    direction = step[0]
    distance = int(step[1:])
    if direction =='R':
        return distance, 0
    elif direction =='L':
        return -distance, 0
    elif direction =='U':
        return 0, distance
    else:
        return 0, -distance        

def popGrid(currX, currY,x, y, numSteps):
    if x==0:
        dist=y
    else:
        dist=x
    #print(dist)
    increment = dist//abs(dist)
    for i in range (increment, dist+increment, increment):
        numSteps+=1
        if x==0:
            #print(currY+i)
            #print(numSteps)
            if (grid[currY+i][currX]==0):
                grid[currY+i][currX]=numSteps
            #print(grid[currY+i])
        else:
            if (grid[currY][currX+i]==0):
                grid[currY][currX+i]=numSteps
    return currX+x, currY+y, numSteps 

def calcManDist (currX, currY, minManDist):
    currManDist= abs(currX-portX) + abs(currY-portY)
    print ("Current:", currManDist, "minManDist: ", minManDist)
    if currManDist < minManDist and currManDist != 0:
        return currManDist
    else:
        return minManDist

def calcMinSteps (numSteps, crossSteps, minSteps):
    currSteps = numSteps + crossSteps
    print ("CurrentSteps:", currSteps, " CrossSteps: ", crossSteps, " minSteps: ", minSteps)
    if currSteps < minSteps and currSteps != 0:
        return currSteps
    else:
        return minSteps

def checkGrid(currX, currY,x, y, grid, numSteps, minSteps):
    #minManDist=manDist
    if x==0:
        dist=y
    else:
        dist=x
    increment = dist//abs(dist)
    for i in range (increment, dist+increment, increment):
        numSteps+=1
        if x==0:
            if grid[currY+i][currX]>0:
                minSteps = calcMinSteps(numSteps, grid[currY+i][currX], minSteps) 
        else:
            if grid[currY][currX+i]>0:
                minSteps = calcMinSteps(numSteps, grid[currY][currX+i], minSteps) 
    return currX+x, currY+y, numSteps, minSteps 



input = open('input.txt', 'r')

wire1 = getWire()
wire2 = getWire()
cols_count = 50000
rows_count = 50000
grid = [[0 for x in range(cols_count)] for x in range(rows_count)]
currX = 10000
currY = 10000
portX = currX
portY = currY
numSteps=0
print(wire1)
print(wire2)

for step in wire1:
    x, y = getSteps(step)
    currX, currY, numSteps = popGrid(currX, currY, x, y, numSteps)
'''currX=portX
currY=portY
for step in wire2:
    x, y = getSteps(step)
    currX, currY = popGrid(currX, currY, x, y)    

#for i in range(0,32):
#    print (grid[100-i])
'''
#for line in grid:
#    print (line)

#print(grid)
minSteps=300000
currX=portX
currY=portY
numSteps=0
for step in wire2:
    x, y = getSteps(step)
    currX, currY, numSteps, minSteps = checkGrid(currX, currY, x, y, grid, numSteps, minSteps)
    #print(minSteps)
    
print(minSteps)
