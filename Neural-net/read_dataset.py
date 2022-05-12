import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def read_dataset(points=144, days=1357):  # returns a python list of 2 dimensions, containing 1357 days with 1440 measurements each
    df = np.zeros((days, points), dtype=np.float32)
    day = np.zeros(points, dtype=np.float32)
    day_counter = 0
    dates = []
    measurement_counter = 0
    per = 1440 / points
    mean = 0  # calculates the mean of the 'extra' points

    with open('./cleaned_dataset.txt', 'r') as file:
        content = file.read().splitlines()
        last_date = None

        for line in content:
            date = line.split(';')[0]
            mean += float(line.split(';')[2])
            if last_date != date and last_date:
                df[day_counter] = day  # adds day by day
                day_counter += 1
                dates.append(date)
                measurement_counter = 0
                if day_counter == days:
                    break

            if measurement_counter % per == 0:
                day[int(measurement_counter / per)] = mean / per  # adds each measurement to the day
                mean = 0
                last_date = date
            measurement_counter += 1

    return df, dates


def preprocess(df):  # normalizes values
    return df / 12


def split_data(X, percentage=5):
    idx = int((1 - percentage / 100) * len(X))  # index at the 95% mark
    X_train = X[:idx]

    X_test = X[idx:]

    return X_train, X_test


if __name__ == '__main__':
    db, dates = read_dataset(days=20)
    x = np.linspace(0, 24, 144)

    X = preprocess(db)

    for i, day in enumerate(db):
        dayy, month, year = dates[i].split('/')
        weekday = datetime(int(year), int(month), int(dayy)).weekday()
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        plt.title(f'{dates[i]} - {week[weekday]}')
        plt.plot(x, day)
        plt.xlabel('hours')
        plt.ylabel('kW')

        plt.show()
