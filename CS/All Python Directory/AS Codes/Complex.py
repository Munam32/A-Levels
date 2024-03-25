unit=50.9
print('x',('--'*10),'MS Shopping Center','--'*10,'x')
item=input('Please Enter The Item You Purchased : ')
quantity=int(input('Please enter the quantity : '))
multiply=int(quantity*unit)
print('The unit Price for',item,'is',unit,'Rs.''You Purchased',quantity,'Kg of',item,)
print('Total Price : ',multiply)
discount=int(input('% Of Discount : '))
discount_multiply=int(((100-discount)/100)*multiply)
save=multiply-discount_multiply
print('You Saved : ',save)
print('Price After Discount : ',discount_multiply)
