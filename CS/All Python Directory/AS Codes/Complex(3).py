design=("x----------------Thank You For Shopping----------------x")
price=int(input("Enter Total Bill : "))
discount_1=int((70/100)*price)
discount_2=int((75/100)*price)
discount_3=int((80/100)*price)
discount_4=int((90/100)*price)
if(price>=10000):
    print("Price After 30% Discount :",discount_1)
    print(design)
elif(price>=8000):
    print("Price After 25% Discount :", discount_2)
    print(design)
elif(price>=5000):
    print("Price After 20% Discount :", discount_3)
    print(design)
elif(price>=2500):
    print("Price After 10% Discount :", discount_4)
    print(design)
else:
    print('Discount Limit not Exceded')
    print("Total Bill :",price)
    print(design)
