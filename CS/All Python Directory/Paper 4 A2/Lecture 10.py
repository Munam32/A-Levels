# Declare Index : Integer               Method 1
Numbers = [10,32,24,56,75,86]
New_array = []
Index = 5
while Index > -1:
    New_array.append(Numbers[Index])
    Index = Index-1
print(New_array)
##########################################################################                  Method 2
# Declare opposite,x : Integer
Numbers = [10,32,24,56,75,86]
new = [0,0,0,0,0,0]
opposite = 5

for x in range(6):
    new[x]=Numbers[opposite]
    opposite = opposite -1
print(new)
##########################################################################
# Declare count,sum : Integer
# Declare flag: Boolean
# Declare average: Real
count = 0
sum = 0
flag = True

while flag:
    Number = float(input("Enter Number: "))
    if Number != 0:
        count = count+1
        sum = sum + Number

    elif(Number == 0):
        flag = False

if count !=0:
    average = sum/count
    print("Average:",average)
##########################################################################



