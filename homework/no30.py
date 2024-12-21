""""30. Write a program to calculate the delivery cost based on the weight of the
package:
 If the package weighs less than 5kg, charge 5.
 If it weighs between 5kg and 20kg, charge 10.
 Check if the delivery is urgent; if yes, add $5 extra."""
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