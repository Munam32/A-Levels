                        # PART 1
arr=[]
for count2 in range(0,3,1):
    value_2=int(input("Enter Values to Enter in Array: "))
    arr.append(value_2)

                        # PART 2

value=int(input("Enter Your Value to check Index Number: "))
for count in range(0,100,1):
    if(arr[0]==value and arr[1]==value and arr[2]==value):
        print("Your Value is stored in all index numbers")
        break

    elif(arr[count]==value):
        print("This Value Has Index Number 0")
        break
    else:
        count=count+1
        if(arr[count]==value):
            print("This Value Has Index Value 1")
            break
        else:
            count=count-1+2
            if(arr[count]==value):
                print("This Value Has Index Number 3")
                break
            else:
                print("Value Not Found")
                break

