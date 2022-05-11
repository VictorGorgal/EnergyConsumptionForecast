# PowerConsumption
Project for the creation of a residential energy consumption dataset

The Arduino is connected via USB to a Raspberry Pi that will be the server for this project. The files read_arduino.py and send_data.py need to be running for the project to work, the file check_data.py should only be run when there is a suspicion that there was a power outage.

First, read_arduino.py requests the arduino to measure the power being consumed at that moment and saves it in the dataset.txt

The send_data.py takes care of the MQTT communication to send the dataset information of a specific day to the mobile application. We are using the mosquitto MQTT Broker

Info currently displayed in the app:

![image](https://user-images.githubusercontent.com/94933775/167912463-8c51e367-5867-4091-b8d1-ef75dcd1cfb0.png)

TODO:
-display the info visualy using graphs
-add excessive energy usage warning
