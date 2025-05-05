### 1
# [reeborg連結](https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json)

# def turn_left_loop():
#     move()
#     turn_left()
#     move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def turn_right_loop():
#     turn_right()
#     move()
#     turn_right()
#     move()

# def move_loop():
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#     move()
#     turn_left()
#     move()

# def total_move():
#     move_loop()
#     move_loop()
#     move_loop()
#     move_loop()
#     move_loop()

# turn_left_loop()
# total_move()
# turn_right_loop()

# 改良
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for i in range(6):
#     jump()

### 2
# [reeborg連結](https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Hurdle%202&url=%2Fworlds%2Ftutorial_en%2Fhurdle2.json)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     jump()

### 3
# [reeborg連結](https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2
# Fsk_menu.json&name=Hurdle%203&url=%2Fworlds%2Ftutorial_en%2Fhurdle3.json)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

### 4
# [reeborg連結](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if wall_in_front() and wall_on_right():
#         turn_left()
#     elif front_is_clear() and wall_on_right():
#         move()
#     elif right_is_clear():
#         turn_right()
#         move()
#         turn_right()
#         move()

### 5
# [reeborg連結](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     elif wall_in_front() and right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear() and right_is_clear():
#         turn_right()
#         move()