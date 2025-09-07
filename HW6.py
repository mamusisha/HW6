# task_1

def char_generator(text):
    for char in text:
        yield char

word = "CODE"
for character in char_generator(word):
    print(character)


# task_2

print()
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

print()
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
print()
score = 0
for question, correct_answer in questions.items():
    user_answer = int(input(f"{question} "))
    points = 10 if user_answer == correct_answer else 0
    score += points
    game_logger.info(f"question: {question} , answer: {user_answer} -- points: {points}")

game_logger.info(f"total score: {score}/50")
print(f"your final score is {score} out of 50 points!")


# task_5

#quiz logger
quiz_logger = logging.getLogger('quiz')
quiz_logger.addHandler(logging.FileHandler('quiz.log'))
quiz_logger.setLevel(logging.INFO)

print()
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
