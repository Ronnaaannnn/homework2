"""32. Create a program that suggests activities based on the weather:
 If the weather is sunny, recommend outdoor activities like hiking or a
picnic.
 If the weather is rainy, check if the user has a raincoat or umbrella:
 If yes, suggest going to a nearby mall or museum.
 If no, recommend staying home and watching movies"""
weather = input("Enter the weather (sunny/rainy): ").lower()

if weather == "sunny":
    print("You can go hiking or have a picnic!")
elif weather == "rainy":
    rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if rain_gear == "yes":
        print("You can go to a nearby mall or museum!")
    else:
        print("It 's best to stay home and watch movies!")
else:
    print("Invalid weather input. Please enter 'sunny' or 'rainy'.")
