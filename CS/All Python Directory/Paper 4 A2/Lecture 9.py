# Declare count,x : Integer
Names = ["Taha","Empty","Empty","Empty","Banto","Empty" ]
count = 0
for x in range(len(Names)):
    if Names[x] == "Empty":
        count = count +1
print(count)
##########################################################################
# Declare sum: Integer
Numbers = [10,12,14,76,34,3,2,23]

sum = 0

for x in range(len(Numbers)):
    if Numbers[x] > 10:
        sum = Numbers[x] + sum
print("The sum of numbers greater than 10 are",sum)
##########################################################################
