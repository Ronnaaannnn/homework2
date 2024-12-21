""""29. Write a program to determine if a candidate is eligible for a job:
 If the candidate's age is >= 18, check if they have a degree.
If they have a degree, check their work experience:
 More than 3 years: Display "Highly Eligible."
 1-3 years: Display "Eligible."
 Less than 1 year: Display "Under Review."""""
age = int(input("Enter your age: "))
degree = input("Do you have a degree? (yes/no): ").lower()
experience = int(input("Enter your work experience in years: "))
if age >= 18:
    if degree == "yes":
        if experience > 3:
            print("Highly Eligible.")
        elif 1 <= experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Degree is required for the job.")
else:
    print("You must be at least 18 years old for the job.")
