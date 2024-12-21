"""13. A company decided to give bonus of 5% to employee if his/her year of
service is more than 5years. Ask user for their salary and year of service
and print the net bonus amount."""
years_of_service = int(input("Enter the number of years of service: "))
salary = float(input("Enter the salary of the employee: "))

if years_of_service > 5:
    bonus = salary * 0.05
else:
    bonus = 0

print(f"The net bonus amount is: Rs {bonus}")
