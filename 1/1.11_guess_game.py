# Написать игру, которая предлагает угадать загаданное число. 
# У игрока есть только 3 попытки.
# Пример вывода:

# (base) genrikh.metlov@b-r7aymd6m-0612 1 % python3 1.11_guess_game.py 
# Guess: 1
# Guess: 2
# Guess: 3
# Sorry, you failed!
# (base) genrikh.metlov@b-r7aymd6m-0612 1 % python3 1.11_guess_game.py
# Guess: 2
# Guess: 9
# You won!































# import random

# secret_num = random.randint(0, 9)
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1

#     if guess == secret_num:
#         print('You won!')
#         break

# else:
#     print("Sorry, you failed!")