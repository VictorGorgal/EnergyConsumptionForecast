# Energy Consumption Forescast
Project for the creation of a residential energy consumption dataset using a raspberry pi as the MQTT Broker together with an LSTM deep neural network running on a mobile app to analyze and display the data privately.

Directories:  
- Arduino/Arduino.ino  - code running on a arduino connected via USB to the Raspberry Pi  
- Neural-net/  - all the files necessary for the creation of the neural network  
- Raspberry/  - all the files that are currently on the Rasp  
- SmartLabApp.zip  - Android Studio project for the mobile app

Info currently displayed in the app:  
![image](https://user-images.githubusercontent.com/94933775/167912463-8c51e367-5867-4091-b8d1-ef75dcd1cfb0.png)

# Current state
The data collecting system and the MQTT protocoll are almost done, the to-do list is on the directiory.  
The neural net is already working and trained, it works with 48 data points at a time, since the data collection system collects every minute, the 1440 daily measurements need to be distilled down to 48, that is done automatically before sending to the MQTT server already.

# To-do
- display the info visualy using graphs  
- implement LSTM neural net in the app  
- add excessive energy usage warning
