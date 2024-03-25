# Declare Guess_Num : Float
# Declare Guess_Name : String

Guess_Num = float(input("Enter Number: "))
Guess_Name = input("Enter Name: ")

if Guess_Num == 20 and Guess_Name == "Munam":
    print("Both are Correct")
elif Guess_Num == 20:
    print("Correct Number but wrong name")
elif Guess_Name:
    print("Correct Name but wrong number")
else:
    print("Aap say nhi ho pae ga")

###############################################################################
# Declare FirstNum,SecondNum,ThirdNum : Float

Firstnum = float(input("Enter Number: "))
Secondnum = float(input("Enter Number: "))
Thirdnum = float(input("Enter Number: "))

if Firstnum>Secondnum and Firstnum>Thirdnum:
    print(Firstnum)
elif Secondnum>Thirdnum and Secondnum>Firstnum:
    print(Secondnum)
else:
    print(Thirdnum)

###############################################################################
# Declare password,email : String

password = input("Enter Password: ")
email = input("Enter Email: ")

if password == "12ab" and email == "123@papersdock.com" :
    print("Both are correct")
else:
    print("Both are Wrong")