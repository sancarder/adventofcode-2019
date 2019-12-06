def read_input():
    input = open('input.txt', 'r')
    intCode = input.readline()
    intCodes = intCode.split(',')
    intCodes =list(map(int, intCodes))
    #print(intCodes)
    opPos = 0
    op=intCodes[opPos]
    
    return op, intCodes, opPos

def addCodes(opPos, intCodes):
    intCodes[intCodes[opPos+3]]=intCodes[intCodes[opPos+1]] + intCodes[intCodes[opPos+2]]  

def multiplyCodes(opPos, intCodes):
    intCodes[intCodes[opPos+3]]=intCodes[intCodes[opPos+1]] * intCodes[intCodes[opPos+2]]  

def run_program(op, intCodes, opPos):

    while op!=99 and opPos < len(intCodes):
        #print (""+ op + " factors: " + intCodes[op+1] + " " +intCodes[op+1])
        if(op==1):
            addCodes(opPos, intCodes)
        elif (op==2):
            multiplyCodes(opPos, intCodes)
        opPos+=4 
        op=intCodes[opPos]

    return intCodes[0]



for noun in range(0,99):
    for verb in range(0,99):
        op, intCodes, opPos = read_input()        

        intCodes[1] = noun
        intCodes[2] = verb

        answer = run_program(op, intCodes, opPos)

        if answer == 19690720:  
            print(noun, verb)
            print(100*noun+verb)
