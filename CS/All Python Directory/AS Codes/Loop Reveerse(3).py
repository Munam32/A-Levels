table=int(input("Enter Table : "))
start=int(input("Enter Start Value : "))
end=int(input("Enter End Value : "))
while(start>=end):
    print(table,"x",start,"=",table*start)
    start=start-1