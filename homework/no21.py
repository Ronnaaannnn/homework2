"""21. Accept the following from the user and calculate the percentage of class
attended:
a. Total number of days
b. Total number of days for absent
After calculating percentage show that, if the percentage is less than 75,
than student will not be able to sit in exam."""
total_days = int(input("Enter the total number of days: "))
absent_days = int(input("Enter the total number of days absent: "))
attended_days = total_days - absent_days
attendance_percentage = (attended_days / total_days) * 100
print(f"Attendance Percentage: {attendance_percentage}%")
if attendance_percentage < 75:
    print("You are not eligible to sit in the exam.")
else:
    print("You are eligible to sit in the exam.")