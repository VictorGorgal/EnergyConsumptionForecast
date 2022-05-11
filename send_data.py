import paho.mqtt.client as paho
import json


def get_data_from_date(date: str):
    """
    :param date: string como '6/5/2022'
    :return: list[float] de todas as medidas salvas daquele dia
    """

    with open('dataset.txt', 'r') as dataset:
        data = dataset.read().splitlines()

    to_return = []
    for line in data:
        info = line.split(';')
        if info[0] == date:
            to_return.append(float(info[2]))

    return to_return


def reduce_data(day: list[float]):
    """
    :param day: lista de todas as medidas salvas de um dia
    :return: list[float] das medidas reduzidas a apenas 48 medidas arredondadas
    """

    to_return = []
    mean = 0
    for i, data in enumerate(day):
        mean += data

        if i % 30 == 0 and i != 0:  # media aritmetica de 30 medidas por vez
            to_return.append(round(mean / 30, 2))
            mean = 0

        if i == 0:  # adiciona a primeira medida do dia sem efetuar a media
            to_return.append(round(mean, 2))

    return to_return


def data_to_json(day: list[float]):
    """
    :param day: lista das medidas reduzidas a apenas 48 medidas
    :return: json das medidas reduzidas a apenas 48 medidas
    """

    to_return = json.dumps(day)
    return to_return


def on_message(client, _, msg):
    payload = msg.payload.decode('ascii')
    if payload.count('/') != 2:
        return

    print(f'Topic:{msg.topic}\nPayload:{payload}')

    day = get_data_from_date(payload)
    day = reduce_data(day)
    day = data_to_json(day)
    print(day)

    # a single publish, this can also be done in loops, etc.
    client.publish(TOPIC, payload=day, qos=1)


def iniciate_MQTT():
    # using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
    # userdata is user defined data of any type, updated by user_data_set()
    # client_id is the given name of the client
    client = paho.Client(client_id=CLIENT_ID, userdata=None, protocol=paho.MQTTv311)

    # enable TLS for secure connection
    # client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    # set username and password
    client.username_pw_set(USERNAME, PASSWORD)
    # connect to HiveMQ Cloud on port 8883 (default for MQTT)
    client.connect(BROKER, PORT)

    # setting callbacks, use separate functions like above for better visibility
    client.on_message = on_message

    # subscribe to all topics of encyclopedia by using the wildcard "#"
    client.subscribe(TOPIC, qos=1)

    # loop_forever for simplicity, here you need to stop the loop manually
    # you can also use loop_start and loop_stop

    print('Ready!')
    client.loop_forever()


if __name__ == '__main__':
    # insert your credentials
    BROKER = 'xxx'  # Ex. 192.168.1.1
    PORT = 1883
    TOPIC = 'home/mobile'
    CLIENT_ID = 'powerdata'
    USERNAME = 'yyy'
    PASSWORD = 'zzz'

    iniciate_MQTT()
    
