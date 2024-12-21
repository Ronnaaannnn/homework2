"""23. Accept the age, gender ('M', 'F'), number of days and display the wages
accordingly.
Age Gender Wage/day
>=18 and <30 M 700
F 750
>=30 and <=40 M 800
F 850"""
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
days = int(input("Enter the number of days worked: "))
if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
    else:
        wage_per_day = 0
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
    else:
        wage_per_day = 0
else:
    wage_per_day = 0

if wage_per_day > 0:
    total_wage = wage_per_day * days
    print(f"Your total wage for {days} days is: Rs {total_wage}")
else:
    print("Invalid input for age or gender.")
