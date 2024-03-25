total_price= 25000.96
amount_r= 23000.58
price_dis=total_price*(90/100)
price=int(price_dis)
balance=amount_r-price_dis
pay=int(balance)
name='Abdul\'s'
design='--'*10

print('Mr.',name,'Billing:')
print('--'*20)
print('Total Amount:',total_price)
print('After 10% discount:',price)
print('Amount Received:',amount_r)
print('Balance:',pay)
print(design,'Thank You For Choosing This Shop',design)
