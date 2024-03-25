# Declare number,divisor : FLOAT
number = float(input("Enter number to be divided: "))
divisor = float(input("Enter Divisor: "))

def div(number,divisor):
    quotient = number // divisor
    return quotient

print("Your whole number is: ",div(number,divisor))
##########################################################################
# Declare number,divisor : Float
number = float(input("Enter number to be divided: "))
divisor = float(input("Enter Divisor: "))

def mod(number,divisor):
    remainder = number % divisor
    return remainder

print("Your remainder is: ",mod(number,divisor))
##########################################################################