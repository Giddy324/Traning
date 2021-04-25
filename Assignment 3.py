# Enter full names
print("Enter First and Last name:")
fname = input("fname:")  # first Name

lname = input("lname:")  # last name

fullnames = fname + "" + lname

# Enter phone ,email

print("Enter customer's phone number:")

phone = input('phone')

print("Enter customer's email:")

email = input("email")

# price of a used car
price = 10000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.02*price
print()
print("full Names:" + fullnames)
print("phone:" + phone)
print("Email:" + email)
# print("Down payment:" +down_payment)
print("Down payment: {:.2f}".format(down_payment))