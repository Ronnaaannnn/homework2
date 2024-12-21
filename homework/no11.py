"""11. A company decided to give bonus to employee according to following
criteria:
Time period of service Bonus
More than 10 years 10%
>=6 and <=10 8%
Less than 6 years 5%"""

years_of_service = int(input("Enter the number of years of service: "))
salary = float(input("Enter the salary of the employee: "))
if years_of_service > 10:
    bonus = salary * 0.10
elif 6 <= years_of_service <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05
print(f"The bonus for an employee with {years_of_service} years of service is: {bonus}")
