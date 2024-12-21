"""Ask the user for a subject score. If it's above 90, congratulate him. If it's
between 50 and 90, suggest improvement. Otherwise, advise on retaking the
course."""
score = float(input("Enter your subject score: "))
if score > 90:
    print("Congratulations! Great job!")
elif 50 <= score <= 90:
    print("Good work! But there's room for improvement.")
else:
    print("You should consider retaking the course.")
