"""36. Create a Python program that greets the user with the message "Welcome to
the Space Mission". Then, ask the user whether they want to go "to the moon"
or "to Mars". If they choose "to Mars", print "Game Over". If they choose "to
the moon", ask if they want to "land on the surface" or "stay in orbit". If they
choose "land on the surface", print "Game Over". If they choose "stay in orbit",
ask them to choose between "alien", "asteroid", or "satellite". If they choose
"alien" or "asteroid", print "Game Over". If they choose "satellite", print "You
Win"."""
print("Welcome to the Space Mission")
destination = input("Do you want to go to the moon or to Mars? ").lower()
if destination == "to mars":
    print("Game Over")
elif destination == "to the moon":
    choice = input("Do you want to land on the surface or stay in orbit? ").lower() 
    if choice == "land on the surface":
        print("Game Over")
    elif choice == "stay in orbit":
        object_choice = input("Do you want to choose alien, asteroid, or satellite? ").lower()
        
        if object_choice == "alien" or object_choice == "asteroid":
            print("Game Over")
        elif object_choice == "satellite":
            print("You Win")
        else:
            print("Invalid choice. Please choose 'alien', 'asteroid', or 'satellite'.")
    else:
        print("Invalid choice. Please choose 'land on the surface' or 'stay in orbit'.")
else:
    print("Invalid choice. Please choose 'to the moon' or 'to Mars'.")
