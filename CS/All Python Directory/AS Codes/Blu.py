def exit():
    input("Press any key to exit")

def main():
    decision=input("You Want To find Factorial Or Base Number? (F/B): ")
    if (decision.lower()=="f"):
        factorial=int(input("Enter The Number you want to find factorial: "))
        Factorial(factorial)
        exit()
    elif(decision.lower()=="b"):
        Basenum=int(input("Enter the factorial for which Base number is to be found: "))
        FindBaseNumber(Basenum)
        exit()

def Factorial(basenum):
    calculation=basenum
    count=basenum
    loop=True
    while loop:
        if count==1:
            print(count)
            loop=False
        count=count-1
        calculation=count*calculation
        if count==1:
            loop=False
            print(calculation)

def FindBaseNumber(factorial):
    global Basenum
    Basenum = -1
    count=0
    loop=True
    calculation=factorial
    while loop:
        count=count + 1
        calculation=calculation/count
        if calculation==1:
            loop=False
            Basenum=count
            print(Basenum)
        else:
            if calculation<1:
                loop=False
                print(Basenum)


main()





