# task_1

def char_generator(text):
    for char in text:
        yield char

word = "CODE"
for character in char_generator(word):
    print(character)