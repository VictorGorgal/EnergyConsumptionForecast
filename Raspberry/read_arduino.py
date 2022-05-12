import serial
from datetime import datetime
from time import sleep

# dataset = 'dataset.txt'  # windows
# node = serial.Serial('COM9', 115200, timeout=5)

dataset = 'Python/dataset.txt'  # raspberry
node = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 115200, timeout=5)


def save(data):
    """
    :param data: measurement to be saved on the dataset.txt
    :return: None
    """
    now = datetime.now()

    mins = now.minute
    hours = now.hour
    day = now.day
    month = now.month
    year = now.year

    # temp = f'{day}/{month}/{year};{hours}:{mins}:0;{data}'  # python 3+
    temp = str(day) + '/' + str(month) + '/' + str(year) + ';' + str(hours) + ':' + str(mins) + ':0;' + str(data) + '\n'  # python 2.7

    with open(dataset, 'a') as file:
        file.write(temp)
    print(temp.replace('\n', ''))


def fix():
    """
    I dont know why but without this func the first line saved will have no measurement
    :return: None
    """
    node.write('send'.encode())
    print('debug: ' + str(node.readline().decode('ascii').strip()))
    node.write('send'.encode())
    print('debug: ' + str(node.readline().decode('ascii').strip()))
    node.write('send'.encode())
    print('debug: ' + str(node.readline().decode('ascii').strip()))
    print('starting....')


fix()

last_minute = -1
while True:
    minutes = datetime.now().minute
    if minutes != last_minute:  # Requests the sensor read every minute
        node.write('send'.encode())
        recieved = node.readline().decode('ascii').strip()
        save(recieved)
        last_minute = minutes

    sleep(5)  # avoids the PC of using 100% CPU
