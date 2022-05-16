# Energy Consumption Forescast
Project for the creation of a residential energy consumption dataset using a raspberry pi as the MQTT Broker together with an LSTM deep neural network running on a mobile app to analyze and display the data privately.

Directories:  
- Arduino/Arduino.ino  - code running on a arduino connected via USB to the Raspberry Pi  
- Neural-net/  - all the files necessary for the creation of the neural network  
- Raspberry/  - all the files that are currently on the Rasp  
- SmartLabApp.zip  - Android Studio project for the mobile app

Info currently displayed in the app:  
![image](https://user-images.githubusercontent.com/94933775/167912463-8c51e367-5867-4091-b8d1-ef75dcd1cfb0.png)

TODO:  
- display the info visualy using graphs  
- implement LSTM neural net in the app  
- add excessive energy usage warning
