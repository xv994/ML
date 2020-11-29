import lost


def get_k_gradient(train_data, k, b):
    step = 0.0000000001  # 1e-10
    gradient = (lost(train_data, k + step, b) - lost(train_data, k, b)) / step
    return gradient


def get_b_gradient(train_data, k, b):
    step = 0.0000000001  # 1e-10
    gradient = (lost(train_data, k, b + step) - lost(train_data, k, b)) / step
    return gradient
