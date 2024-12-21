"""Write a program to accept the cost price of a bike qnd display the road tax
to be paid according to the following criteria:
Cost price (in Rs) Tax"""

cost_price = float(input("Enter the cost price of the bike (in Rs): "))

if cost_price > 100000:
    tax = (cost_price * 15) / 100
elif cost_price > 50000 and cost_price <= 100000:
    tax = (cost_price * 10) / 100
else:
    tax = (cost_price * 5) / 100

print(f"The road tax to be paid is: Rs {tax}")
