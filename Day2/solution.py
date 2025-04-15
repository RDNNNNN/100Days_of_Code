print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

if tip == 10:
    tip = bill * 1.1
elif tip == 12:
    tip = bill * 1.12
elif tip == 15:
        tip = bill * 1.15

people = int(input("How many people to split the bill?"))

result = round((tip / 100 * bill + bill) / people , 2)

print(f"Each person should pay: ${result}")