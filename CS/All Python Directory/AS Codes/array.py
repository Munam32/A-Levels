total=0
arr=[]
for count in range(0,5,1):
    value=int(input("Enter Value: "))
    arr.append(value)
    total=total+arr[count]
print("Total:",total)
