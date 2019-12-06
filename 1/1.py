input = open('input.txt', 'r')

sums = 0

for mass in input:
    
    fuel = int(mass)
    
    while fuel >0:
        fuel = int(fuel)//3 -2
        if fuel > 0:
            sums += fuel
    
print(sums)
