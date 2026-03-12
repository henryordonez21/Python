import random

def roll():
    return random.randint(1,6)

while True:
    players = input("Enter number of players between 2 - 4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Not a valid number")
    else:
        print("Invalid input")

max_score = 50
player_scores = [0] * players

while max(player_scores) < max_score:
    for player_index in range(players):
        print("Players", player_index + 1, "has just started")
        print("Total score is", player_scores[player_index], "\n")
        current_score =0
        while True:
            should_roll = input("Would you like to roll? (y): ")
            if should_roll.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("You rolled a 1!, Turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a ", value)

            print("Your score is:", current_score)
        
        player_scores[player_index] += current_score
        print("Total score is", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player" , winning_index + 1, "won with a score of" ,max_score)
