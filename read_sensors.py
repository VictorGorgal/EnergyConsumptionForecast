import serial
from datetime import datetime
from time import sleep

# dataset = 'dataset.txt'  # windows
# node = serial.Serial('COM9', 115200, timeout=5)

dataset = 'Python/dataset.txt'  # raspberry
node = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 115200, timeout=5)


def save(data):
    """
    :param data: medida a ser salva no dataset
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
    Por algum motivo se nao rodar esta funcao, a primeira linha eh salva sem medida
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
    if minutes != last_minute:  # requisita a leitura do sensor a cada minuto
        node.write('send'.encode())
        recieved = node.readline().decode('ascii').strip()
        save(recieved)
        last_minute = minutes

    sleep(5)  # evita o programa de usar 100% do CPU
