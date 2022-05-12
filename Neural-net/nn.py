import read_dataset as rds
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


EPOCHS = 10
BATCH_SIZE = 64

POINTS = 48  # entire project revolves on just 48 points


# using more days seemed to have a negative impact
df, dates = rds.read_dataset(points=POINTS, days=500)
dataset = rds.preprocess(df)

train, test = rds.split_data(dataset)
train = train.flatten()
train = train.reshape((len(train), 1))

train_generator = TimeseriesGenerator(train, train,
                                      length=POINTS,
                                      sampling_rate=1, stride=1,
                                      batch_size=BATCH_SIZE)

neurons = 144

model = Sequential()
model.add(LSTM(neurons, input_shape=(POINTS, 1), return_sequences=True))
model.add(LSTM(1, input_shape=(neurons,), return_sequences=True))
model.add(LSTM(neurons, input_shape=(1,)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

history = model.fit(train_generator, epochs=EPOCHS)

model.save('main_model.h5')

plt.plot(history.history['loss'])
plt.title('model loss')
plt.show()
