table = int(input("Enter Your table value: "))
start = int(input("Enter Start Value : "))
end = int(input("Enter End Value : "))
for s in range(start, end - 1, -1):
    print(table, "x", s, "=", table * s)
for b in range(0,1000,1):
    ans=input("Do You Want To Continue again ?(y/n) : ")
    if(ans=="y"):
        table = int(input("Enter Your table value: "))
        start = int(input("Enter Start Value : "))
        end = int(input("Enter End Value : "))
        for s in range(start, end - 1, -1):
            print(table, "x", s, "=", table * s)
    else:
        break







