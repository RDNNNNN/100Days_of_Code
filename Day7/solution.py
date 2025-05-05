import random

letter = ["red", "green", "blue"]

HANGMAN = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

ans = random.choice(letter)

placeholder = "_" * len(ans)

guessed_letters = []

lives = 6

start = True

while start:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in ans:
        if letter == guess:
            display += letter
            guessed_letters.append(letter)
            print("猜對囉")
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"

    if guess not in guessed_letters:
        lives -= 1
        print("猜錯囉哈哈")
        if lives == 0:
            start = False
            print("你是輸家哭著回家找媽媽!!")

    if "_" not in display:
        print("你是贏家!!")
        break

    print(display)
    print(f"你還剩餘 {lives} 條命")
    print(HANGMAN[lives])

# string

# guessed = ""
# while True:
#     guess = input("Guess a letter: ").lower()

#     if guess in ans and guess not in guessed:
#         guessed += guess

#     display = ""
#
#     for letter in ans:
#         if letter in guessed:
#             display += letter
#         else:
#             display += "_"
#     print(display)

#     if "_" not in display:
#         print("YOU ARE WINNER!!")
#         break












