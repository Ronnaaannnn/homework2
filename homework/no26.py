""""26. Ask a user for a username and password. If the username is correct, check if
the password is correct, and display appropriate login messages."""
username = input("Enter your username: ")
password = input("Enter your password: ")
correct_username = "user123"
correct_password = "password123"
if username == correct_username:
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password. Try again.")
else:
    print("Incorrect username. Try again.")

