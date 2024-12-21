"""35. Create a Python program that greets the user with the message "Welcome to
the Magic Forest". Then, ask the user whether they want to go "north" or
"south". If they choose "south", print "Game Over". If they choose "north", ask
if they want to "cross the river" or "follow the path". If they choose "cross the
river", print "Game Over". If they choose "follow the path", ask them to choose
between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy", print "Game
Over". If they choose "elf", print "You Win"."""
print("Welcome to the Magic Forest")
direction = input("Do you want to go north or south? ").lower()
if direction == "south":
    print("Game Over")
elif direction == "north":
    choice = input("Do you want to cross the river or follow the path? ").lower()
    if choice == "cross the river":
        print("Game Over")
    elif choice == "follow the path":
        creature_choice = input("Do you want to choose fairy, ogre, or elf? ").lower()
        
        if creature_choice == "ogre" or creature_choice == "fairy":
            print("Game Over")
        elif creature_choice == "elf":
            print("You Win")
        else:
            print("Invalid choice. Please choose 'fairy', 'ogre', or 'elf'.")
    else:
        print("Invalid choice. Please choose 'cross the river' or 'follow the path'.")
else:
    print("Invalid choice. Please choose 'north' or 'south'.")
