def set_status(previous, current):
    
    if current == 0:
        status = 0
    elif current == 1:
        status = 1
    elif current == 2:
        status = previous
        
    return status

input = open('input.txt', 'r')

pixelstring = input.readline()
pixels = list(map(int, pixelstring.strip()))
nr_of_pixels = len(pixels)

#Real input
width = 25
height = 6

#Test input
#width = 2
#height = 2

prop = width * height

layermap = {}
layercount = 0

for i in range(0, nr_of_pixels, prop):
    layercount +=1
    layermap[layercount] = pixels[i:i+prop]
    #print(layermap[layercount])

positionList = []

positionstatus = {}

for i in range(0, prop):
    current = -1
    positionList.append(2)
    for layer in range(layercount, 0, -1):
        #print(layermap[layer])
        current = layermap[layer][i]
        #positionmap[i].append(current)
        positionList[i] = set_status(positionList[i], current)
    #print(positionList, " ", current)
        

print('\n')
print(positionList[0:25])
print(positionList[25:50])
print(positionList[50:75])
print(positionList[75:100])
print(positionList[100:125])
print(positionList[125:150])

