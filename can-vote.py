# Program to take an age as an input and display if the user can vote.
## A user can vote if his age is greater than or equal to 18


age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("Sorry! You cannot vote")
