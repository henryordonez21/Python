print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "c":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "g":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "r":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "p":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")