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

def popGrid(currX, currY,x, y):
    if x==0:
        dist=y
    else:
        dist=x
    #print(dist)
    increment = dist//abs(dist)
    for i in range (increment, dist+increment, increment):
        if x==0:
            #print(currY+i)
            grid[currY+i][currX]=1
            #print(grid[currY+i])
        else:
            grid[currY][currX+i]=1
    return currX+x, currY+y 

def calcManDist (currX, currY, minManDist):
    currManDist= abs(currX-portX) + abs(currY-portY)
    print ("Current:", currManDist, "minManDist: ", minManDist)
    if currManDist < minManDist and currManDist != 0:
        return currManDist
    else:
        return minManDist

def checkGrid(currX, currY,x, y, grid, minManDist):
    #minManDist=manDist
    if x==0:
        dist=y
    else:
        dist=x
    increment = dist//abs(dist)
    for i in range (increment, dist+increment, increment):
        if x==0:
            if grid[currY+i][currX]==1:
                minManDist = calcManDist( currX, currY+i, minManDist) 
        else:
            if grid[currY][currX+i]==1:
                minManDist = calcManDist( currX+i, currY, minManDist) 
    return currX+x, currY+y, minManDist 



input = open('input.txt', 'r')

wire1 = getWire()
wire2 = getWire()
cols_count = 50000
rows_count = 50000
grid = [[0 for x in range(cols_count)] for x in range(rows_count)]
currX = 5000
currY = 5000
portX = currX
portY = currY
print(wire1)
print(wire2)

for step in wire1:
    x, y = getSteps(step)
    currX, currY = popGrid(currX, currY, x, y)
'''currX=portX
currY=portY
for step in wire2:
    x, y = getSteps(step)
    currX, currY = popGrid(currX, currY, x, y)    

#for i in range(0,32):
#    print (grid[100-i])
for line in grid:
    print (line)
#print(grid)
'''
manDist=10000
currX=portX
currY=portY
for step in wire2:
    x, y = getSteps(step)
    currX, currY, manDist = checkGrid(currX, currY, x, y, grid, manDist)
    print(manDist)
    
print(manDist)
