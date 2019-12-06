input = open('input.txt', 'r')

sums = 0

for mass in input:
    sums += int(mass)//3 -2
    
print(sums)
