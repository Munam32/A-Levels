design="x-----------------------------Admission Form-----------------------------X"
print(design)
religion=input("Enter Your Religion : ")
age=int(input("Enter Your Age : "))
job=input("Enter Your Previous Job : ")

if((age<=26 and age>=18) and(religion.lower()=="islam" or religion.lower()=="christianity") and (job.lower()=="teacher" or job.lower()=="clerk")):
    print("Your Admission has been approved")
else:
    print("Sorry, You Are Not Selected")
print(design)