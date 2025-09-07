# task_1

def char_generator(text):
    for char in text:
        yield char

word = "CODE"
for character in char_generator(word):
    print(character)


# task_2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    try:
        index = int(input("enter index: "))
        print(f"element: {arr[index]}")
    except (ValueError, IndexError):
        print("invalid input or index out of range.")
    if input("continue? (y/n): ").lower() != 'y':
        break