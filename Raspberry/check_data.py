from datetime import datetime, timedelta


class MissingMeasurement(Exception):
    """
    Exception raised when there is no measurement on a dataset line
    """
    def __init__(self, line):
        self.message = f'Missing power measurement on line: {line}'
        super().__init__(self.message)


class MissingDate(Exception):
    """
    Exception raised when there is a missing line on the dataset
    """
    def __init__(self, line):
        date = line_to_datetime(line) - timedelta(minutes=1)
        date = date.strftime('%d/%m/%Y;%H:%M:%S;x.xx')
        self.message = f'Expected {date} before {line}'
        super().__init__(self.message)


def line_to_datetime(line: str):
    """
    :param line: Single dataset line
    :return: datetime object from the input line
    """
    date, time, power = line.split(';')

    if not power:
        raise MissingMeasurement(line)

    return datetime.strptime(f'{date} {time}', '%d/%m/%Y %H:%M:%S')


if __name__ == '__main__':
    with open('dataset.txt', 'r') as dataset:
        data = dataset.read().splitlines()[1:]

    date = line_to_datetime(data[0])  # inicial date
    for line in data:
        if date != line_to_datetime(line):
            raise MissingDate(line)

        date += timedelta(minutes=1)

    print('Dataset is ready!')
