# Declare Fullname,Firstname,Lastname: String
Fullname = "Taha Ali"
Firstname = Fullname[0:4]
Lastname = Fullname[5:8]
print("Your First Name is: ",Firstname)
print("Your Last Name is: ",Lastname)
##########################################################################
fullname = input("Enter Full name: ")
lastnameindex = 0
for x in range(len(fullname)):

    if fullname[x:x+1] == " ":
        print("Your First Name is:",fullname[0:x])
        lastnameindex = len(fullname)-x

    if lastnameindex!=0 :
        if(x == len(fullname)-1):
            print("Your Last name is:",fullname[lastnameindex:x+1])




