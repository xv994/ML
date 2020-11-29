import random


def get_train_data():
    x = 0.
    y = 0.
    train_data = [[0. for i in range(0)] for i in range(10)]
    for i in range(1, 11):
        y = 7 * i + 2 + random.random() * 1     # 上下浮动0.5
        x = i - 1 + random.random() * 1             # 上下浮动0.5
        train_data[i - 1].append(x)
        train_data[i - 1].append(y)
    return train_data


def lost(train_data, k, b):
    _lost_ = 0
    for i in range(0, len(train_data)):
        _lost_ += (train_data[i][1] - k * i - b) ** 2
    return _lost_


def get_k_gradient(train_data, k, b):
    step = 0.0000000001  # 1e-10
    gradient = (lost(train_data, k + step, b) - lost(train_data, k, b)) / step
    return gradient


def get_b_gradient(train_data, k, b):
    step = 0.0000000001  # 1e-10
    gradient = (lost(train_data, k, b + step) - lost(train_data, k, b)) / step
    return gradient


a = 0.0000002  # learning rate
e = 3  # extreme

train_data = [[1.1124025695834623, 10.438418251387022], [1.550402679019413, 17.04254713925447], [2.642100313684801, 24.272027614407794], [4.093688582858903, 31.03709783632702], [4.962636307735583, 38.327468575323806], [5.743708158032248, 45.35414471019414], [6.843106464951109, 52.4807052336535], [7.73945894062078, 59.007588059228496], [8.98509506017786, 65.54209020709976], [10.079959244832846, 72.57869902441513]]
# train_data = get_train_data()

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

k = 0.1  # initial value of slop
b = 0.1  # initial value off y-intercept
# i = 0
__lost__ = lost(train_data, k, b)

# print(train_data)
# print(k, b)
# print(__lost__)

while __lost__ > e:
    k -= get_k_gradient(train_data, k, b) * a
    b -= get_b_gradient(train_data, k, b) * a
    __lost__ = lost(train_data, k, b)
# i = i + 1
# print(i)
print(__lost__)

# print(k)
# print(b)
if b > 0:
    print("y=" + str(k) + "x+" + str(b))
else:
    print("y=" + str(k) + "x" + str(b))


