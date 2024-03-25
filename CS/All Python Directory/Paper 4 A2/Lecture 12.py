def table(num):

    for x in range(11):
        print(str(num) + " " + "x" + " " + str(x) + " " + "=" + " " + str(num*x))

table(5)
##########################################################################
# Declare num : Integer
Numbers = [45,34,23,87,96,23]

def FindLargestNum(large):
    largenum=0
    for x in range(len(large)):
        if large[x] > largenum:
            largenum = large[x]
    return largenum

num = FindLargestNum(Numbers)

table(num)
##########################################################################
