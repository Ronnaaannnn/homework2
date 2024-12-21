"""18. Accept any city from the user and display monument of that city.
City Monument
Delhi Red Fort
Agra Taj Mahal
Jaipur Jal Mahal"""
city = input("Enter the name of the city: ").lower()

if city == "delhi":
    print("The monument in Delhi is the Red Fort.")
elif city == "agra":
    print("The monument in Agra is the Taj Mahal.")
elif city == "jaipur":
    print("The monument in Jaipur is the Jal Mahal.")
else:
    print("Monument information for this city is not available.")
