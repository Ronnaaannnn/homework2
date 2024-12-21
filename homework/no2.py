#2.Create a Python program that starts by greeting the user with a message
#"Welcome to Treasure Land". Then, prompt the user to choose a direction,
#either "left" or "right". If the user chooses "right", print "Game Over". If the user
#chooses "left", ask whether they want to "swim" or "wait". If they choose
#"swim", print "Game Over". If they choose to "wait", ask them to select a color:
#"red", "blue", or "yellow". If the user picks "blue" or "red", print "Game Over". If
#they select "yellow", print "You Win

print("Welcome to Treasure Land")
direction = input("Choose a direction: left or right? ").lower()

if direction == "right":
    print("Game Over")
elif direction == "left":
    action = input("Do you want to swim or wait? ").lower()
    if action == "swim":
        print("Game Over")
    elif action == "wait":
        color = input("Choose a color: red, blue, or yellow? ").lower()
        if color == "blue" or color == "red":
            print("Game Over")
        elif color == "yellow":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")
