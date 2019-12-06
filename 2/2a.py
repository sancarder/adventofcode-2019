def addCodes(opPos, intCodes):
    intCodes[intCodes[opPos+3]]=intCodes[intCodes[opPos+1]] + intCodes[intCodes[opPos+2]]  

def multiplyCodes(opPos, intCodes):
    intCodes[intCodes[opPos+3]]=intCodes[intCodes[opPos+1]] * intCodes[intCodes[opPos+2]]  

input = open('input.txt', 'r')
intCode = input.readline()
intCodes = intCode.split(',')
intCodes =list(map(int, intCodes))
print(intCodes)
opPos = 0
op=intCodes[opPos]

while op!=99:
    #print (""+ op + " factors: " + intCodes[op+1] + " " +intCodes[op+1])
    if(op==1):
        addCodes(opPos, intCodes)
    elif (op==2):
        multiplyCodes(opPos, intCodes)
    opPos+=4 
    op=intCodes[opPos]

print(intCodes[0])
