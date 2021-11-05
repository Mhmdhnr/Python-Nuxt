import random
from models.random_x_y import RandomXY


def get_x_y(count):
    x_y_list: list[RandomXY] = []
    for n in range(count):
        x = n + 1
        y = random.randint(1500, 2000)
        x_y_list.append(RandomXY(x, y))
    return x_y_list
