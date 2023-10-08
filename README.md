# Energy Consumption Forescast
Project for the creation of a residential energy consumption dataset using a raspberry pi as the MQTT Broker together with an LSTM deep neural network running on a mobile app to analyze and display the data privately.

Directories:  
- Arduino/Arduino.ino  - code running on a arduino connected via USB to the Raspberry Pi  
- Neural-net/  - all the files necessary for the creation of the neural network  
- Raspberry/  - all the files that are currently on the Rasp  
- SmartLabApp.zip  - Android Studio project for the mobile app

# LSTM Neural Network

Original dataset used: www.kaggle.com/datasets/uciml/electric-power-consumption-data-set

Due to some days in the dataset having missing lines, there was a need to clean the dataset, we removed all the days that had a missing measurement.  
It is possible to visualy see the data separated in each day with the read_dataset.py file. 
![image](https://user-images.githubusercontent.com/94933775/168104463-d8ed6fdd-d7bf-4d6b-bb41-2515032c7d74.png)

New prediction example (dotted line):  
![image](https://user-images.githubusercontent.com/94933775/168108476-2b1e36c3-1c0d-4865-a110-7ad95e09c36a.png)
