def read_input():
    input = open('input.txt', 'r')
    intCode = input.readline().strip()
    intCodes = intCode.split(',')
    intCodes = list(map(int, intCodes))
    #print(intCodes)
    opPos = 0
    op=intCodes[opPos]
    
    return op, intCodes, opPos

def getParamMode(op, param):
    #Example op=10102 param = 2
    opString =str(op)
    if op < 10:
        return 0
    else:
        if param == 1:
            return int(opString[len(opString)-3])
        elif param == 2:
            if op < 1000:
                return 0 
            else:
                return int(opString[len(opString)-4])
        elif param == 3:
            if op < 10000:
                return 0 
            else:
                return int(opString[0])
        
def getValue(opPos, intcodes, op, param):
    if getParamMode(op, param) == 0:
        return intCodes[intCodes[opPos]]
    else:
        return intCodes[opPos]


def addCodes(opPos, intCodes, op):
    term1 = getValue(opPos+1, intCodes, op, 1)
    term2 = getValue(opPos+2, intCodes, op, 2)
    if getParamMode(op, 3) == 0:
        intCodes[intCodes[opPos+3]] = term1 + term2 
    else:
        intCodes[opPos+3] = term1 + term2 


def multiplyCodes(opPos, intCodes, op):
    term1 = getValue(opPos+1, intCodes, op, 1)
    term2 = getValue(opPos+2, intCodes, op, 2)
    if getParamMode(op, 3) == 0:
        intCodes[intCodes[opPos+3]] = term1 * term2
    else:
        intCodes[opPos+3] = term1 * term2

def storeInput(opPos, intCodes, inputValue):
    intCodes[intCodes[opPos+1]] = inputValue 

def outPutValue(opPos, intCodes):
    print(intCodes[intCodes[opPos+1]]) 


def parseOp(op):
    if op < 10:
        return op
    else:
        opString = str(op)
        return int(opString[len(opString)-2:])

def run_program(op, intCodes, opPos, inputValue):

    while op != 99 and opPos < len(intCodes):
        opCode = parseOp(op)
        if(opCode == 1):
            addCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 2):
            multiplyCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 3):
            storeInput(opPos, intCodes, inputValue)
            numberOfParams = 2
        elif (opCode == 4):
            outPutValue(opPos, intCodes)
            numberOfParams = 2
        opPos += numberOfParams 
        op = intCodes[opPos]

    return "Stopped"

inputValue = 1
#print(parseOp(102))
op, intCodes, opPos = read_input()        
answer = run_program(op, intCodes, opPos, inputValue)
print(answer)