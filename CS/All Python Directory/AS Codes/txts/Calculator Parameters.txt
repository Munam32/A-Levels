def out(a,b):
    for count in range(1,b+1,1):
        print(a,"x",count,"=",a*count)
        print("---------------------------------")

a=int(input("Enter Value: "))
b=int(input("Enter Value of Table: "))
print("---------------------------------")
out(a,b)
