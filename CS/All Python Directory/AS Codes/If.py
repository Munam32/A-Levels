design='--'*20
option_1='Addition'
option_2='Subtraction'
option_3='Multiplication'
option_4='Division'
print('Menu :')
print(design)
print('1)',option_1,'          2)',option_2)
print('3)',option_3,'          4)',option_4)
print(design)
choice=input('Enter Your choice : ')
number_1=int(input('Enter 1st Number : '))
number_2=int(input('Enter 2nd Number : '))
if(choice=='1'):
    print('Adding',number_1,'and',number_2,'is :',number_1+number_2)
if(choice=='2'):
    print('Subtracting',number_1,'and',number_2,'is :',number_1-number_2)
if(choice=='3'):
    print('Multiplying',number_1,'and',number_2,'is :',number_1*number_2)
if(choice=='4'):
    print('Dividing',number_1,'and',number_2,'is :',number_1/number_2)
