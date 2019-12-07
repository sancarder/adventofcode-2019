#range = 357253-892942 Sandra
#range = 273025-767253 Mattias

def check_length(password):
    if len(password) == 6:
        return True
    else:
        return False

def check_increase(password):
    numbers = list(password)
    status = True
    for n in range(0,len(numbers)-1):
        if (numbers[n] > numbers[n+1]):
            status = False
            break

    return status

def check_double_digits(password):
    numbers = list(password)
    status = False
    #lastGroupPos = 0
    #Treat first character as special case
    if numbers[0]==numbers[1]:
        status = True
    
    for n in range(1,len(numbers)-1):
        if (numbers[n] == numbers[n+1]):
            if numbers[n-1] != numbers[n]:
                status = True
            else:
                status = False

    return status

def run_all():

    numbers_of_passwords = 0
    for i in range(273025, 767253):
        password = str(i)
        length = check_length(password)
        increase = check_increase(password)
        double_digits = check_double_digits(password)
        
        if length and increase and double_digits:
            numbers_of_passwords += 1
            print(password)
        
    print(numbers_of_passwords)
    
def run_test():

    numbers_of_passwords = 0

    for i in [111111, 223450, 123789, 112233, 123444, 111122]:
        password = str(i)
        print(password)
        length = check_length(password)
        print(length)
        increase = check_increase(password)
        print(increase)
        double_digits = check_double_digits(password)
        print(double_digits)
        print('\n')
        
        if length and increase and double_digits:
            numbers_of_passwords += 1
        
    print(numbers_of_passwords)

run_test()
#run_all()

    
