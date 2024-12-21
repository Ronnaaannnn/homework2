"""Take two numbers and find the greater of the two. If they are equal, check if
the number is positive, negative, or zero."""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("The numbers are equal.")
    if num1 > 0:
        print("The number is positive.")
    elif num1 < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
