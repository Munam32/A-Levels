n1=int(input("Enter Your First Number : "))
n2=int(input("Enter Your Second Number : "))
n3=int(input("Enter Your Third Number : "))
n4=int(input("Enter Your Fourth Number : "))
if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            print("1st Number Is Greatest")
        else:
            print("4th Number is greatest")
    else:
        if(n3>n4):
            print("3rd Number is greatest")
else:
    if(n2>n3):
        if(n2>n4):
            print("2nd number is greatest")
        else:
            print("4th number is greatest")
    else:
        if(n3>n4):
            print("3rd number is the greatest")