import lost

def get_gradient(k):
    step = 0.0000000001  # 1e-10
    gradient = (lost(k + step) - lost(k)) / step
    return gradient
