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
        
def getValue(opPos, intCodes, op, param):
    if getParamMode(op, param) == 0:
        return intCodes[intCodes[opPos]]
    else:
        return intCodes[opPos]


def addCodes(opPos, intCodes, op):
    term1 = getValue(opPos+1, intCodes, op, 1)
    term2 = getValue(opPos+2, intCodes, op, 2)
    print(term1, term2, intCodes)
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

def run_program(op, intCodes, opPos, inputValue, phase, firstRun):
    outValue = 0
    firstInput = True
    print("Input: ", inputValue)
    while op != 99 and opPos < len(intCodes):
        opCode = parseOp(op)
        print("opPos: ", opPos, " opCode: ", opCode)
        print(intCodes)
        if(opCode == 1):
            addCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 2):
            multiplyCodes(opPos, intCodes, op)
            numberOfParams = 4
        elif (opCode == 3):
            if firstInput == True and firstRun == True:
                storeInput(opPos, intCodes, phase)
                print ('Input stored')
                firstInput = False
            else:
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
        op =  intCodes[opPos]
        if opCode == 4:
           return op, intCodes, opPos, outValue


    return op, intCodes, opPos, outValue

OP = 0
INTCODES = 1
OPPOS = 2
PHASE = 3
phases = [5,6,7,8,9]
perm = itertools.permutations(phases)
#print(parseOp(102))
maxThrust = 0
#for x in range (0,1):
ampKeys = ['A', 'B', 'C','D','E']
ampMap = {}
for phaseList in list(perm):
    inputValue = 0
    firstRun = True
    #print(phaseList)
    #for phase in phaseList:
     #   op, intCodes, opPos = read_input()
    
   # ampMap['A'] = [op, intCodes, opPos, phaseList[0]] 
    #phase_test = [9, 8, 7, 6, 5]
    #for phase in phaseList:
    for i in range(0,5):
        op, intCodes, opPos = read_input()
        #ampMap[ampKeys[i]] = [op, intCodes, opPos, phase_test[i]]
        #uncomment below line to run
        ampMap[ampKeys[i]] = [op, intCodes, opPos, phaseList[i]]
    #print (ampMap[amp][OP], ampMap[amp][INTCODES], ampMap[amp][OPPOS], inputValue, ampMap[amp][PHASE], firstRun)
    #inputValue = 0
    #firstRun = True 

    while (op != 99):
        for amp in ampMap:      
            print(op)
            print ('amp: ', amp, inputValue, ampMap[amp][PHASE])
            op, intCodes, opPos, inputValue = run_program(ampMap[amp][INTCODES][ampMap[amp][OPPOS]], ampMap[amp][INTCODES], ampMap[amp][OPPOS], inputValue, ampMap[amp][PHASE], firstRun)
            if op  == 99:
                break
            #print (op, opPos)
            ampMap[amp] = [op, intCodes, opPos, inputValue]
        firstRun = False
    print ('One round done')
    if ampMap['E'][PHASE] > maxThrust:
            maxThrust = ampMap['E'][PHASE]
print(maxThrust)