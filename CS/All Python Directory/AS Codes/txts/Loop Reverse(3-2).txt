table=int(input("Enter Table : "))
start=int(input("Enter Start Value : "))
end=int(input("Enter End Value : "))
end=end-1
for s in range(start,end,-1):
    print(table,"x",s,"=",table*s)