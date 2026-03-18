import random

play = input("Hi, would you like to play? ")

if play.lower() != "yes":
    quit()

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
secret_word = random.choice(words)
score = 0

while True:
    score += 1
    guess = input("Make a guess: ").strip().lower()

    if not guess.isalpha():
        print("That's not a word")
        continue

    if guess == secret_word:
        print("That's correct")
        break
    else:
        print("That's wrong")
        
print("You guessed the word in" , score , "tries")


   



