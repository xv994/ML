# y = 7x + 3
import random


def get_train_data():
    x = 0.
    y = 0.
    train_data = [[0 for i in range(0)] for i in range(100)]
    for i in range(0, 100):
        y = 7 * i + 3 + random.random() * 2
        x = i + random.random() * 2
        train_data[i].append(x)
        train_data[i].append(y)
    return train_data

