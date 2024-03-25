# Declare user : String
def greeting(name):
    print("Hello" + " " + name)

user = input("Enter name: ")
greeting(user)
##########################################################################
# Declare sum,count : Float
def average(Sum,Count):
    print(Sum/Count)

sum = float(input("Enter Sum: "))
count = float(input("Enter Count Value: "))

average(sum,count)

##########################################################################
# Declare sum2: Integer
def Sum(FirstNum,SecondNum,ThirdNum):
    sum = FirstNum + SecondNum + ThirdNum
    return sum

sum2 = Sum(567,543,23)
print(sum2)
##########################################################################