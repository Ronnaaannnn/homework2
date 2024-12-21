"""22. Write a program to accept percentage and display the category according to
the following criteria:
Percentage Category
<40 Failed
>=40 and <55 Fair
>=55 and <65 Good
>=65 Excellent"""
percentage = float(input("Enter your percentage: "))
if percentage < 40:
    category = "Failed"
elif 40 <= percentage < 55:
    category = "Fair"
elif 55 <= percentage < 65:
    category = "Good"
else:
    category = "Excellent"
print(f"Your category is: {category}")
