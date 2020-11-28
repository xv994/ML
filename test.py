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


def lost(train_data, k, b):
    lost_ = 0
    for i in range(0, len(train_data)):
        lost_ += (train_data[i][1] - k * i - b) ** 2
    return lost_


def get_gradient(train_data, k, b):
    step = 0.1  # 1e-10
    gradient = (lost(train_data, k + step, b) - lost(train_data, k, b)) / step
    return gradient


a = 1  # learning rate
e = 100  # extreme
train_data = get_train_data()

# y = kx + b
k = 1.  # slop
b = 1.  # y-intercept

# average value
# list_x = [get_train_data[i][0] for i in range(100)]
# list_y = [get_train_data[i][1] for i in range(1)]
sum_x = 0.
sum_y = 0.
for i in range(len(train_data)):
    sum_x += train_data[i][0]
    sum_y += train_data[i][1]
average_x = sum_x / len(train_data)
average_y = sum_y / len(train_data)

# print(average_x, average_y)

k = random.randint(1, 10)  # initial value of slop
b = average_y - k * average_x
i = 0

while lost(train_data, k, b) > e:
    k -= get_gradient(train_data, k, b) * a
    b = average_y - k * average_x
    i = i + 1
    print(i)

print("y = " + k + "x + " + b)



