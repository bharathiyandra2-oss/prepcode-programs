password=input("enter password:")
special=any(not c.isalnum() for c in password)
print(len(password)>=8 and special)