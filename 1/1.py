input = open('input.txt', 'r')

sums = 0

for line in input:
    
    linesum = round(int(line)/3) -2
    sums += linesum
    
print(sums)
