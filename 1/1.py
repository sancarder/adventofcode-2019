input = open('input.txt', 'r')

sums = 0

for line in input:
    
    sums += int(line)//3 -2
    
print(sums)
