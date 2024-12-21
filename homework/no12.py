"""12. Accept the number of days from the user and calculate the charge for
library according to following:
Till five days: Rs 2/day
Six to ten days: Rs 3/day
11 to 15 days: Rs 4/day
After 15 days: Rs 5/day"""
days = int(input("Enter the number of days: "))

if days <= 5:
    charge = days * 2
elif 6 <= days <= 10:
    charge = days * 3
elif 11 <= days <= 15:
    charge = days * 4
else:
    charge = days * 5

print(f"The charge for {days} days is {charge}")

