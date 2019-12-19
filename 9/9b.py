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
        
def getValue(opPos, intCodes, op, param, relBase):
    #print(opPos, op, param, relBase, len(intCodes))
    if getParamMode(op, param) == 0:
        return intCodes[intCodes[opPos]]
    elif getParamMode(op, param) == 2:
        return intCodes[intCodes[opPos]+relBase]
    else:
        return intCodes[opPos]


def addCodes(opPos, intCodes, op, relBase):
    term1 = getValue(opPos+1, intCodes, op, 1, relBase)
    term2 = getValue(opPos+2, intCodes, op, 2, relBase)
    #print(term1, term2, intCodes)
    if getParamMode(op, 3) == 0:
        intCodes[intCodes[opPos+3]] = term1 + term2
    elif getParamMode(op, 3) == 2:
        intCodes[intCodes[opPos+3]+relBase] = term1 + term2
    else:
        intCodes[opPos+3] = term1 + term2 


def multiplyCodes(opPos, intCodes, op, relBase):
    term1 = getValue(opPos+1, intCodes, op, 1, relBase)
    term2 = getValue(opPos+2, intCodes, op, 2, relBase)
    if getParamMode(op, 3) == 0:
        intCodes[intCodes[opPos+3]] = term1 * term2
    elif getParamMode(op, 3) == 1:
        intCodes[opPos+3] = term1 * term2
    else:
        intCodes[intCodes[opPos+3]+relBase] = term1 * term2


def storeInput(op, opPos, intCodes, inputValue, relBase):
    #print ("storepos", opPos)
    if getParamMode(op, 1) == 2:
        intCodes[intCodes[opPos+ 1]+relBase] = inputValue 
    else:    
        intCodes[intCodes[opPos+1]] = inputValue 

def outPutValue(opPos, intCodes, op, relBase):
    #print ("relBaseOutPut: ", relBase, "opPos: ", opPos)
    if getParamMode(op, 1) == 1:
        #print ("relBaseOutPut: ", relBase)
        #print (intCodes, "opPos: ", opPos)
        value = intCodes[opPos+1] 
        #print(value)
    elif getParamMode(op, 1) == 2:
        value = intCodes[intCodes[opPos+1]+relBase] 
    else:
        value = intCodes[intCodes[opPos + 1]]
    
    #print(value)
    return value    

def jumpIfTrue(opPos, intCodes, op, relBase):
    value = getValue(opPos+1, intCodes, op, 1, relBase)
    if value == 0:
        return 3, 0 #numberOfParams is 3 and nothing else happens
    else:
        return 0, getValue(opPos+2, intCodes, op, 2, relBase)

def jumpIfFalse(opPos, intCodes, op, relBase):
    value = getValue(opPos+1, intCodes, op, 1, relBase)
    #print ("jiff: ", value)
    if value == 0:
        return 0, getValue(opPos+2, intCodes, op, 2, relBase)
    else:
        return 3, 0 #numberOfParams is 3 and nothing else happens

def lessThan(opPos, intCodes, op, relBase):
    term1 = getValue(opPos+1, intCodes, op, 1, relBase)
    term2 = getValue(opPos+2, intCodes, op, 2, relBase)
    #print (term1 , " " , term2)
    if getParamMode(op, 3) == 2:
        address = intCodes[opPos+3]+relBase
    else:
        address = intCodes[opPos+3]
    if term1 < term2:
        intCodes[address] = 1
    else:
        intCodes[address] = 0

def equalTo(opPos, intCodes, op, relBase):
    term1 = getValue(opPos+1, intCodes, op, 1, relBase)
    term2 = getValue(opPos+2, intCodes, op, 2, relBase)
    if getParamMode(op, 3) == 2:
        address = intCodes[opPos+3]+relBase
    else:
        address = intCodes[opPos+3]
    if term1 == term2:
        intCodes[address] = 1
    else:
        intCodes[address] = 0

def parseOp(op):
    if op < 10:
        return op
    else:
        opString = str(op)
        return int(opString[len(opString)-2:])

def run_program(op, intCodes, opPos, inputValue):
    relBase = 0
    outValue = 0
    firstInput = True
    #print("Input: ", inputValue)
    while op != 99 and opPos < len(intCodes):
        opCode = parseOp(op)
        #print("opPos: ", opPos, " opCode: ", opCode, " RelBase: ", relBase, "mem 101: ", intCodes[101])
        #print(intCodes)
        if(opCode == 1):
            addCodes(opPos, intCodes, op, relBase)
            numberOfParams = 4
        elif (opCode == 2):
            multiplyCodes(opPos, intCodes, op, relBase)
            numberOfParams = 4
        elif (opCode == 3):
            '''if firstInput == True and firstRun == True:
                storeInput(opPos, intCodes, phase)
                print ('Input stored')
                firstInput = False
            else:
            '''
            storeInput(op, opPos, intCodes, inputValue, relBase)

            numberOfParams = 2
        elif (opCode == 4):
            outValue = outPutValue(opPos, intCodes, op, relBase)
            numberOfParams = 2
            print ("OutValue: ", outValue)
        elif (opCode == 5):
            numberOfParams, opMove = jumpIfTrue(opPos, intCodes, op, relBase)
            if numberOfParams != 3:
                opPos = opMove
        elif (opCode == 6):
            numberOfParams, opMove = jumpIfFalse(opPos, intCodes, op, relBase)
     #       print ("jumpnumparams: ", numberOfParams, "opPos: ", opPos)
            if numberOfParams != 3:
                opPos = opMove
        elif (opCode == 7):
            lessThan(opPos, intCodes, op, relBase)
            numberOfParams = 4
        elif (opCode == 8):
            equalTo(opPos, intCodes, op, relBase)
            numberOfParams = 4
        elif (opCode == 9):
            relBase += getValue(opPos+1, intCodes, op, 1, relBase)
            #print (relBase)
            numberOfParams = 2


        opPos += numberOfParams 
        op =  intCodes[opPos]
        #if opCode == 4:
        #   return op, intCodes, opPos, outValue


    return op, intCodes, opPos, outValue

OP = 0
INTCODES = 1
OPPOS = 2
PHASE = 3
inputValue = 2
memSize = 10000
intCodes = [0] * memSize
op, intCodesStart, opPos = read_input()
for i in range(0,len(intCodesStart)):
    intCodes[i] = intCodesStart[i]
#print(intCodes)
run_program(op, intCodes, opPos, inputValue)
