import random
import os
from telnetlib import DO
from time import sleep

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1
    
    def move(self, x, y):
        self.y += y
        self.x += x       

class Commander:
    def move(self, who):
        x = random.randint(-1, 1) # -1, 0, 1
        y = random.randint(-1, 1) # -1, 0, 1
        who.move(x, y)


commander = Commander()

robots = []
for i in range(10):
    robots.append(Robot(0, 0))


while True:
    # Хитрый способ очистить экран
    os.system('clear')
    # os.system('CLS')  # in Windows

    # Рисуем воображаемую сетку. Сетка начинается от -30 до 30 по X,
    # и от 12 до -12 по Y
    for y in range(-12, 12):
        for x in range(-30, 30):
            found = False
            for robot in robots:
                if robot.x == x and robot.y == y:
                    found = True

            # Если найден, рисуем звездочку, иначе точку
            if found == True:
                print('🤖', end='')
            else:
                # print('🌾', end='')
                print('🌵', end='')
            
        # Просто переводим строку:
        print('')


    # Каждого робота двигаем в случайном направлении
    for robot in robots:
        commander.move(robot)

    # Задержка в полсекунды
    sleep(0.5)
