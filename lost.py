
def lost(train_data, k, b):
    lost = 0
    for i in range(0, len(train_data)):
        lost += (train_data[i][1] - k * i - b) ** 2
    return lost
