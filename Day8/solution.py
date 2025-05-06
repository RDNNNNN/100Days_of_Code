def greet():
    print("1")
    print("2")
    print("3")

greet()

def life_in_weeks(age):
    age_weeks = (90 - age) * 48
    print(f"You have {age_weeks} weeks left")
    return age_weeks

life_in_weeks(56)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("bea", "taipei")
greet_with(name="bea",location="taipei")

# 先把名字拆開
# 依序檢查名字是否有包含 TRUE LOVE 單字
# 把 TRUE 的結果加起來
# 把 LOVE 的結果加起來
# TRUE 當成第一位數
# LOVE 當成第二位數
# 最後組成二位數

def calculate_love_score(name1,name2):
    first_num = 0
    sec_num = 0

    for i in (name1 + name2).lower():
        if i in "true":
            first_num += 1

        if i in "love":
            sec_num += 1
    print(f"{first_num}{sec_num}")

calculate_love_score(name1="Angela Yu",name2="Jack Bauer")

# 錯誤的邏輯
# def calculate_love_score(name1, name2):
#     first_total = 0
#     sec_total = 0
#     name1 = name1.lower()
#     name2 = name2.lower()
#     for i in name1:
#         if i == "t" or i == "r" or i == "u" or i == "e":
#             first_total +=1
#         elif i == "l" or i == "o" or i == "v" or i == "e":
#             sec_total +=1

#     for i in name2:
#         if i == "t" or i == "r" or i == "u" or i == "e":
#             first_total += 1
#         elif i == "l" or i == "o" or i == "v" or i == "e":
#             sec_total += 1
#     print(f"Total: {first_total}")
#     print(f"Total: {sec_total}")
#     print(str(first_total) + str(sec_total))

