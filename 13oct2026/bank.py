balance=25000
amount=int(input("enter withdrawal amount:"))
print(amount<=balance and amount%500==0 and amount>0)