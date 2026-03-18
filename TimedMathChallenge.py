import random
import time

OPERATORS = ["+","-","*"]
MIN_NUMBER = 3
MAX_NUMBER = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    
    left = random.randint(MIN_NUMBER,MAX_NUMBER)
    right = random.randint(MIN_NUMBER,MAX_NUMBER)
    operator = random.choice(OPERATORS)
    expr = (f"{left} {operator} {right}")
    answer = eval(expr)

    return expr,answer


input("Press ENTER to play! ")
print("------------------")
start_time = time.time()
wrong = 0

for i in range(TOTAL_PROBLEMS):

    expr,answer = generate_problem()
    
    while True:
        guess = input(f"Problem {i+1} answer: {expr} = ")
        if guess.isdigit and int(guess )== answer:
            break
        wrong += 1

end_time = time.time()
final_time = round(end_time - start_time,2)

print("---------------------------------------")
print(f"You finished in {final_time} seconds!")
print("Wrong answers", wrong)
    

