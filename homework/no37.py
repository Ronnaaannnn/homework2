"""37. Create a Python program that greets the user with the message "Welcome to
the Pirate Island". Then, ask the user whether they want to go "left" or "right".
If they choose "right", print "Game Over". If they choose "left", ask if they want
to "dig for treasure" or "sail the ship". If they choose "dig for treasure", print
"Game Over". If they choose "sail the ship", ask them to choose between
"shark", "pirate ship", or "mermaid". If they choose "shark" or "pirate ship",
print "Game Over". If they choose "mermaid", print "You Win"."""
print("Welcome to the Pirate Island!")
direction = input("Do you want to go 'left' or 'right'? ").lower()
if direction == "right":
    print("Game Over")
elif direction == "left":
    action = input("Do you want to 'dig for treasure' or 'sail the ship'? ").lower()
    
    if action == "dig for treasure":
        print("Game Over")
    elif action == "sail the ship":
        creature = input("Do you want to encounter a 'shark', 'pirate ship', or 'mermaid'? ").lower()
        
        if creature == "shark" or creature == "pirate ship":
            print("Game Over")
        elif creature == "mermaid":
            print("You Win")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")