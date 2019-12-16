import itertools

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

def outPutValue(opPos, intCodes, op):
    if getParamMode(op, 1) == 1:
        value = intCodes[opPos+1] 
        #print(value)
    else:
        value = intCodes[intCodes[opPos+1]]
        #print(value)
    return value    

def jumpIfTrue(opPos, intCodes, op):
    value = getValue(opPos+1, intCodes, op, 1)
    if value == 0:
        return 3, 0 #numberOfParams is 3 and nothing else happens
    else:
        return 0, getValue(opPos+2, intCodes, op, 2)

def jumpIfFalse(opPos, intCodes, op):
    value = getValue(opPos+1, intCodes, op, 1)
    if value == 0:
        return 0, getValue(opPos+2, intCodes, op, 2)
    else:
        return 3, 0 #numberOfParams is 3 and nothing else happens

def lessThan(opPos, intCodes, op):
    term1 = getValue(opPos+1, intCodes, op, 1)
    term2 = getValue(opPos+2, intCodes, op, 2)
    #print (term1 , " " , term2)
    if term1 < term2:
        intCodes[intCodes[opPos+3]] = 1
    else:
        intCodes[intCodes[opPos+3]] = 0

def equalTo(opPos, intCodes, op):
    term1 = getValue(opPos+1, intCodes, op, 1)
    term2 = getValue(opPos+2, intCodes, op, 2)
    if term1 == term2:
        intCodes[intCodes[opPos+3]] = 1
    else:
        intCodes[intCodes[opPos+3]] = 0

def parseOp(op):
    if op < 10:
        return op
    else:
        opString = str(op)
        return int(opString[len(opString)-2:])

def run_program(op, intCodes, opPos, inputValue, phase):
    outValue = 0
    firstInput = True
    #print("Input: ", inputValue, " Phase: ", phase)
    while op != 99 and opPos < len(intCodes):
       
        opCode = parseOp(op)
        #print("opPos: ", opPos, " opCode: ", opCode)
        #print(intCodes)
        if(opCode == 1):
            addCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 2):
            multiplyCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 3):
            if firstInput == True:
                storeInput(opPos, intCodes, phase)
              #  print ("Phase: ", phase)
                firstInput = False
            else:
             #   print ("Input: ", inputValue)
                storeInput(opPos, intCodes, inputValue)
            numberOfParams = 2
        elif (opCode == 4):
            outValue = outPutValue(opPos, intCodes, op)
            numberOfParams = 2
            print ("OutValue: ", outValue)
        elif (opCode == 5):
            numberOfParams, opMove = jumpIfTrue(opPos, intCodes, op)
            if opMove != 0:
                opPos = opMove
        elif (opCode == 6):
            numberOfParams, opMove = jumpIfFalse(opPos, intCodes, op)
            if opMove != 0:
                opPos = opMove
        elif (opCode == 7):
            lessThan(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 8):
            equalTo(opPos, intCodes, op)
            numberOfParams = 4

        opPos += numberOfParams 
        op = intCodes[opPos]

    return outValue

phases = [1,0,4,3,2]
perm = itertools.permutations(phases)
#print(parseOp(102))
maxThrust = 0
for phaseList in list(perm):
    inputValue = 0
    #print(phaseList)
    for phase in phaseList:
        op, intCodes, opPos = read_input()        
        inputValue = run_program(op, intCodes, opPos, inputValue, phase)
    if inputValue > maxThrust:
        maxThrust = inputValue
print(maxThrust)
