# task_1

print("\ntask_1")
def char_generator(text):
    for char in text:
        yield char

word = "CODE"
for character in char_generator(word):
    print(character)


# task_2

print("\ntask_2")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    try:
        index = int(input("enter index: "))
        print(f"element: {arr[index]}")
    except (ValueError, IndexError):
        print("invalid input or index out of range.")
    if input("continue? (y/n): ").lower() != 'y':
        break


# task_3

print("\ntask_3")
def counter(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.count += 1
        print(f"call: {func.count}")
        return func(*args, **kwargs)
    return wrapper

@counter
def say():
    print("Hi")

for _ in range(5):
    say()


# task_4

import logging

print("\ntask_4")

#game logger
game_logger = logging.getLogger('game')
game_logger.addHandler(logging.FileHandler('game.log'))
game_logger.setLevel(logging.INFO)

questions = {
    "15 + 27?": 42,
    "8 * 9?": 72,
    "144 / 12?": 12,
    "25 - 13?": 12,
    "7 * 7": 49
}
score = 0
for question, correct_answer in questions.items():
    user_answer = int(input(f"{question} "))
    points = 10 if user_answer == correct_answer else 0
    score += points
    game_logger.info(f"question: {question} , answer: {user_answer} -- points: {points}")

game_logger.info(f"total score: {score}/50")
print(f"your final score is {score} out of 50 points!\n")


# task_5

print("\ntask_5")

#quiz logger
quiz_logger = logging.getLogger('quiz')
quiz_logger.addHandler(logging.FileHandler('quiz.log'))
quiz_logger.setLevel(logging.INFO)

def quiz_generator():
    questions1 = [
        "capital of france?",
        "2 + 2?",
        "mix red and blue?",
        "largest planet in our solar system?",
        "best programming language?"
    ]
    for q in questions1:
        yield q

for question in quiz_generator():
    answer = input(f"{question} :")
    quiz_logger.info(f"question: {question} - answer: {answer}")
quiz_logger.info("\n")


#task_6

print("\ntask_6")

import random

rps_logger = logging.getLogger('rps')
rps_logger.addHandler(logging.FileHandler('rps.log'))
rps_logger.setLevel(logging.INFO)

choices = ['rock', 'paper', 'scissor']
wins = {'rock': 'scissor', 'paper': 'rock', 'scissor': 'paper'}
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player = input("rock, paper, or scissor? ").lower()
    if player not in choices:
        print("invalid! try again.")
        continue
    computer = random.choice(choices)
    if player == computer:
        result = "it's a tie!"
    elif wins[player] == computer:
        result = "player wins!"
        player_score += 1
    else:
        result = "computer wins!"
        computer_score += 1
    rps_logger.info(f"player: {player}, computer: {computer}, result: {result}")

print(f"{"player" if player_score == 3 else "computer"} won the game.")
rps_logger.info(f"{"player" if player_score == 3 else "computer"} won the game!")




