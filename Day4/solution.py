import random

friends = ["Alice", "Bob", "Charlie", "David", "Emu"]

print(random.choice(friends))
print(friends[random.randint(0,4)])
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = int(input("""What do your choose?
Type 0 for Rock, 1 for Paper or 2 for Scissors.
"""))

data = [rock,paper,scissors]
num = random.randint(0,2)

if choose == num:
    print(data[choose])
    print(f" Computer chose:{data[num]}")
    print("Tie!")
elif choose == 0 and num == 1 or choose == 1 and num == 2 or choose == 2 and num == 0:
    print(data[choose])
    print(f" Computer chose:{data[num]}")
    print("You Lose!")
elif choose == 0 and num == 2 or choose == 1 and num == 0 or choose == 2 and num == 1:
    print(data[choose])
    print(f" Computer chose:{data[num]}")
    print("You Win!")
else:
    print("Please input 0 or 1 or 2")


