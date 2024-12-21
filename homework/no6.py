#6. WAP which accepts marks of four subjects and display total marks,
#percentage and grade

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))

total_marks = subject1 + subject2 + subject3 + subject4
percentage = (total_marks / 400) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Grade: {grade}")
