"""34. Create a Python program that greets the user with the message "Welcome to
the Jungle Adventure". Then, ask the user whether they want to go "left" or
"right". If they choose "right", print "Game Over". If they choose "left", ask if
they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
print "Game Over". If they choose "explore the cave", ask them to choose"""
print("Welcome to the Jungle Adventure!")
direction = input("Do you want to go left or right? ").lower()
if direction == "right":
    print("Game Over")
elif direction == "left":
    choice = input("Do you want to climb a tree or explore the cave? ").lower()
    if choice == "climb a tree":
        print("Game Over")
    elif choice == "explore the cave":
        cave_choice = input("Do you want to enter the cave or stay outside? ").lower()
        
        if cave_choice == "enter the cave":
            print("You found treasure! Congratulations!")
        elif cave_choice == "stay outside":
            print("You wait outside and enjoy the peaceful jungle.")
        else:
            print("Invalid choice. Please choose again.")
    else:
        print("Invalid choice. Please choose 'climb a tree' or 'explore the cave'.")
else:
    print("Invalid choice. Please choose 'left' or 'right'.")
