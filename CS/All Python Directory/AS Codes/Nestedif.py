design=("--------------------- Admission Form ---------------------")
print(design)
entry_test=int(input("Enter % of marks gained in entry test : "))
if(entry_test>=90):
    a_level = int(input("Enter % of marks gained in A Levels : "))
    if(a_level>=90):
        o_level = int(input("Enter % of marks gained in O Levels : "))
        if(o_level>=90):
            print("You Are Allotted Section \'A\'")
        else:
            print("You Are Allotted Section \'B\'")
    else:
        print("You Are Allotted Section \'C\'")
else:
    print("Sorry, No Admission")
print(design)
