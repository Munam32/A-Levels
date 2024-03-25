month_days=31
def fun1_allowance(grade,d):
    if(grade>=1 and grade<=10):
        d=int(d*(110/100))
        return d
    else:
        if(grade>=11 and grade<=20):
            d = int(d * (120 / 100))
            return d

def fun2(f,c,d):
    day_1=int(f/month_days)
    amount_to_deduct=int(c*day_1)
    deducted_amount=d-amount_to_deduct
    return deducted_amount

def main():
    print("Grades → 1-10 , 11-20")
    grade=int(input("Enter Your Grade: "))
    fun1_allowance(grade,0)
    if(grade>=1 and grade<=10):
        salary=int(input("Enter Salary: "))
        print("After 10% Allowance:",fun1_allowance(grade,salary))
        allowance=fun1_allowance(grade,salary)
        absent_days=int(input("Enter Number Of Absent Days: "))
        print("Your Salary After Deduction:",fun2(salary,absent_days,allowance))
    else:
        if(grade>=11 and grade<=20):
            salary = int(input("Enter Salary: "))
            print("After 20% Allowance:", fun1_allowance(grade,salary))
            allowance = fun1_allowance(grade,salary)
            absent_days = int(input("Enter Number Of Absent Days: "))
            print("Your Salary After Deduction:", fun2(salary, absent_days, allowance))




main()






