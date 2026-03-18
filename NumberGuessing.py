import random

guesses = input("Enter the number of guesses: ")

if guesses.isdigit():
   guesses = int(guesses)

else:
   print("That's not a valid entry")
   quit()

random_number = random.randint(1,guesses)
score = 0

while True:
    score += 1
    user_guess = input("Enter a number: ")

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
       print("That's not a valid number")
       continue

    if user_guess > random_number:
       print("Too High!")
    elif user_guess < random_number:
       print("Too Low!")

    if user_guess == random_number:
       print("That's correct!")
       print("You got it correct after" ,score, "tries")
       break



