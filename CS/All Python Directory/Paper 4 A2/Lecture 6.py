# Declare Positive_Count,Negative_Count : Integer
# Declare number: Float

Positive_Count = 0
Negative_Count = 0
for x in range(5):
    number = float(input("Enter Number: "))

    if number>0:
        Positive_Count = Positive_Count+1
    elif(number<0):
        Negative_Count = Negative_Count+1

print("Numbers that are positive:",Positive_Count)
print("Numbers that are negative:",Negative_Count)

##################################################################################
# Declare smallest_value, number: Float
smallest_value = 9999.0

for x in range(5):
    number = float(input("Enter Number: "))

    if number<smallest_value:
        smallest_value = number
print(smallest_value)

##################################################################################

