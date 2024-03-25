n1=int(input("Enter Your First Number : "))
n2=int(input("Enter Your Second Number : "))
n3=int(input("Enter Your Third Number : "))
if(n1<n2):
    if(n1<n3):
        print("First Number:",n1,"is The Least")
    else:
        if(n3<n2):
            print("Third Number:",n3,"is The Least")
        else:
            if(n2<n1):
                print("Second Number:", n1, "is The Least")
            else:
                print("First Number:",n1,"is The Least")
else:
    if(n2<n3):
        print("Second Number:",n2,"is The Least")
    else:
        print("Third Number:",n3,"is The Least")