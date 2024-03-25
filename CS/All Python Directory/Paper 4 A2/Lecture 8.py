##########################################################################
# Declare Length: Integer
Names = ["Taha","Ahmed","Pappu","Bano","Banto","Pappan"]
Length = len(Names)
print(Length)
##########################################################################
# Declare x: Integer
for x in range(len(Names)):
    print(Names[x])
##########################################################################
# Declare  Index : Integer
# Declare Break : Boolean
Index = -1
Break = True

while Index<6 and Break:
    Index = Index +1
    if Names[Index] == "Bano":
        Break = False
print(Index)
##########################################################################
for x in range(len(Names)):
    if Names[x] == "Bano":
        print(x)
##########################################################################
Names.append("Shabnam")
print(Names)
##########################################################################
NewName = input("Enter Name: ")
Present = False

for x in range(len(Names)):
    if NewName == Names[x]:
        Present = True
if Present == False:
    Names.append(NewName)
else:
    print("This name is already present")






