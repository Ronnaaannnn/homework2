""""31. Write a program to check if a user qualifies for a loan:
 If the user's income is above 50,000, check their credit score:
 If the credit score is above 700, approve the loan.
 If the credit score is between 600 and 700, approve with a
higher interest rate.
 If the credit score is below 600, reject the loan."""
weight = float(input("Enter the weight of the package (in kg): "))
urgent = input("Is the delivery urgent? (yes/no): ").lower()
if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 20
if urgent == "yes":
    cost += 5
print(f"The total delivery cost is: ${cost}")
