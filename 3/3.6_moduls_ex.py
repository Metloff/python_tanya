# Задание: в предыдущих уроках мы писали программу, которая находит максимальное число в массиве.
# Необходимо на основе нее сделать функциюю finx_max(numbers) и запихнуть ее в модуль utils (utils.find_max(numbers)) 
# numbers = [10, 3, 2, 16, 7]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number

# print(max)

import utils

numbers = [10, 3, 2, 16, 7]

print(utils.find_max(numbers))
print(max(numbers))

# max - встроенная функция которая создана точно так же как и наша find_max