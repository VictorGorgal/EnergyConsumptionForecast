import random
from keras.models import load_model
import read_dataset
import numpy as np
import matplotlib.pyplot as plt

POINTS = 48
BATCH = 32


def add(array, element):
    new = np.zeros(array.shape)
    new[0, :-1, 0] = array[0, 1:, 0]
    new[0, -1, 0] = element
    return new


def predict(model, data, future=144):
    y_hat = []
    for _ in range(future):
        pred = model.predict(data)[0, 0]

        y_hat.append(pred)
        data = add(data, pred)

    return y_hat


model = load_model('main_model.h5')


df, _ = read_dataset.read_dataset(points=POINTS)
dataset = read_dataset.preprocess(df)
train, test = read_dataset.split_data(dataset, percentage=5)

ds = test

print(f'dataset length: {len(ds)}')

while True:
    i = random.randint(0, len(ds) - 1)
    print(f'day #{i}')
    X = ds[i]
    X = X.reshape((1, len(X), 1))
    y = ds[i + 1]

    y_hat = predict(model, X, future=POINTS)

    x = np.linspace(0, 24, POINTS)
    plt.title('Main Model')
    plt.plot(x, X.flatten() * 12, label='base')
    x = np.linspace(24, 48, POINTS)
    plt.plot(x, y.flatten() * 12, label='actual')
    plt.plot(x, np.array(y_hat) * 12, linestyle=':', label='predicted')
    plt.xlabel('Time')
    plt.ylabel('kW')
    plt.legend(loc='upper left')

    plt.show()
