# y = 7x + 3
import random

def get_train_data():
    x = 0.
    y = 0.
    x_y = []
    for i in range(1, 100):
        y = 7 * i + 3 + random.random() * 2
        x = i + random.random() * 2
        x_y[i][0] = x
        x_y[i][1] = y
    return x_y
