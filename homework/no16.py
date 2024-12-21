"""16. N students take K apples and distribute them among each other evenly. The
remaining (the indivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket? The
program reads the numbers N and K. It should print the two answers for the
questions above."""
N = int(input("Enter the number of students (N): "))
K = int(input("Enter the number of apples (K): "))

if N > 0:
    apples_per_student = K // N
    appless = K % N
    print(f"Each student gets {apples_per_student} apples.")
    print(f"{appless} apples remain in the basket.")
else:
    print("Number of students must be greater than 0.")