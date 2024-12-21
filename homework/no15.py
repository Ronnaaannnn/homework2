"""15. A school decided to replace the desks in three classrooms. Each desk sits
two students. Given the number of students in each class, print the smallest
possible number of desks that can be purchased. The program should read
three integers: the number of students in each of the three
classes, a, b and c respectively."""
a = int(input("Enter the number of students in class A: "))
b = int(input("Enter the number of students in class B: "))
c = int(input("Enter the number of students in class C: "))
total_students = a + b + c
if total_students % 2 == 0:
    desks_needed = total_students // 2
else:
    desks_needed = total_students // 2 + 1
print(f"The smallest possible number of desks that need to be purchased: {desks_needed}")
