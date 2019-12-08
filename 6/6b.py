def check_steps(currentObject):
    
    step_map = {}
    steps = 0
    
    while currentObject in orbitMap:
        steps += 1
        step_map[orbitMap[currentObject]] = steps
        currentObject = orbitMap[currentObject]
        
    return step_map


input = open('input.txt', 'r')

orbitMap = {}

for line in input:
    v, k = line.strip().split(')')
    orbitMap[k] = v
    
#print(orbitMap)

youObj = orbitMap["YOU"]
sanObj = orbitMap["SAN"]

you_steps = check_steps(youObj)
san_steps = check_steps(sanObj)


min_steps = 1000000

for k in you_steps:
    if k in san_steps:
        total_steps = you_steps[k] + san_steps[k]
        if total_steps < min_steps:
            min_steps = total_steps
            
print(min_steps)
        
