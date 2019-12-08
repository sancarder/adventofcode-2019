input = open('input.txt', 'r')

orbitMap = {}

for line in input:
    v, k = line.strip().split(')')
    orbitMap[k] = v
    
print(orbitMap)
orbits = 0

for k in orbitMap:
    currentObject = k
    while currentObject in orbitMap:
        orbits += 1
        currentObject = orbitMap[currentObject]
        
        
print(orbits)
        
