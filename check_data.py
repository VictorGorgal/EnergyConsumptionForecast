from datetime import datetime, timedelta


class MissingMeasurement(Exception):
    """
    excecao quando nao ha medida na linha do dataset
    """
    def __init__(self, line):
        self.message = f'Missing power measurement on line: {line}'
        super().__init__(self.message)


class MissingDate(Exception):
    """
    excecao quando falta uma linha no data set
    """
    def __init__(self, line):
        date = line_to_int(line) - timedelta(minutes=1)
        date = date.strftime('%d/%m/%Y;%H:%M:%S;x.xx')
        self.message = f'Expected {date} before {line}'
        super().__init__(self.message)


def line_to_int(line: str):
    """
    :param line: unica linha do dataset
    :return: int dia, mes, ano, hora, minuto, segundo, float potencia
    """
    date, time, power = line.split(';')

    if not power:
        raise MissingMeasurement(line)

    return datetime.strptime(f'{date} {time}', '%d/%m/%Y %H:%M:%S')


with open('dataset.txt', 'r') as dataset:
    data = dataset.read().splitlines()[1:]


date = line_to_int(data[0])  # data inicial
for line in data:
    if date != line_to_int(line):
        raise MissingDate(line)

    date += timedelta(minutes=1)


print('Dataset is ready!')
