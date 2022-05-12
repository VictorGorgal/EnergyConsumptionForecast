read_arduino.py and send_data.py need to be running for the project to work.

check_data.py should only be run when there is a suspicion that there was a power outage.

graph_data.py is used to visually see the data with graphs.


First, read_arduino.py requests the arduino to measure the power being consumed at that moment and saves it in the dataset.txt, send_data.py takes care of the MQTT communication to send the dataset information of a specific day to the mobile app. We are using the mosquitto MQTT Broker
