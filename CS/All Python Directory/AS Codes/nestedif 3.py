n1=int(input("Enter Your 1st Number : "))
n2=int(input("Enter Your 2nd Number : "))
n3=int(input("Enter Your 3rd Number : "))
n4=int(input("Enter Your 4th Number : "))
n5=int(input("Enter Your 5th Number : "))
if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            if(n1>n5):
                print("1st Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
        else:
            if(n4>n5):
                print("4th Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
    else:
        if(n3>n4):
            if(n3>n5):
                print("3rd Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
        else:
            if(n4>n5):
                print("4th Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
else:
    if(n2>n3):
        if(n2>n4):
            if(n2>n5):
                print("2nd Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
        else:
            if(n4>n5):
                print("4th Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
    else:
        if(n3>n4):
            if(n3>n5):
                print("3rd Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
        else:
            if(n4>n5):
                print("4th Number Is The Greatest")
            else:
                print("5th Number Is The Greatest")
