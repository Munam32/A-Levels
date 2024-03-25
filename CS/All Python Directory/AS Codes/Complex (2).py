unit=50.9
print('x',('--'*10),'MS Shopping Center','--'*10,'x')
item=input('Please Enter The Item You Purchased : ')
quantity=int(input('Please enter the quantity : '))
multiply=int(quantity*unit)
print('The unit Price for',item,'is',unit,'Rs.''You Purchased',quantity,'Kg of',item,)
print('Total Price : ',multiply)
discount_1=int((80/100)*multiply)
discount_2=int((90/100)*multiply)
if(multiply>=3000):
    print("Price after 20% Discount : ",discount_1)
else:
    print("Price After 10% Discount : ",discount_2)

