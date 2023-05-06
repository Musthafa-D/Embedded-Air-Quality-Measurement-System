#Importing the necessary libraries as well as necessary values from other tasks
import RPi.GPIO as RPi
import requests
import json
from statistics import mean
from matplotlib import pyplot as plt
import dht11
import time
from collections import deque
#Importing necessary values from Task1
from Task1 import *

field_66 = list(map(float, field6))
#Converting the temperatures from fahrenheit to degree celsius
field_6_C = []
for i in field_66:
    C = (i-32)*(5/9)
    field_6_C.append(C)
    i = i + 1
field_6_degC = list(map(float, field_6_C))
field_77 = list(map(float, field7))

#Storing both field list values as deque
field_6_degC = deque(field_6_degC)
field_77 = deque(field_77)

#Using RPi.GPIO library to use DHT11 Sensor to measure local temperature and humidity values
RPi.setwarnings(False)
RPi.cleanup()
RPi.setmode(RPi.BCM)

while True:
    for i in range (0, 100):
        #Reading data via pin 4
        instance = dht11.DHT11(pin=4)
        result = instance.read()

        #Reading until valid values
        while not result.is_valid():
            result = instance.read()
        temperature = result.temperature
        humidity = result.humidity

        #FIFO Buffer
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)

        field_6_degC.append(temperature)
        field_77.append(humidity)

        field_6_degC.popleft()
        field_77.popleft()

        time.sleep(10)

        #Calculating the mean values of both readings
        mean_field6_degC = mean(field_6_degC)
        print("Mean Temeperature Value is ", mean_field6_degC)
        mean_field7 = mean(field_77)
        print("Mean Humidity Value is ", mean_field7)

        #Plotting the respective temperature and humidity values
        plt.subplot(3, 2, 1)
        plt.plot(range(0, 100), field_11, 'rd-')
        plt.axhline(y=mean_field1, color='r', linestyle='--')
        plt.xlabel("sample")
        plt.ylabel("PM 1.0 (ATM)")
        plt.title("Field 1 Chart")

        plt.subplot(3, 2, 2)
        plt.plot(range(0, 100), field_22, 'ko-')
        plt.axhline(y=mean_field2, color='black', linestyle='--')
        plt.xlabel("sample")
        plt.ylabel("PM 2.5 (ATM)")
        plt.title("Field 2 Chart")

        plt.subplot(3, 2, 3)
        plt.plot(range(0, 100), field_33, 'bo-')
        plt.axhline(y=mean_field3, color='b', linestyle='--')
        plt.xlabel("sample")
        plt.ylabel("PM 10 (ATM)")
        plt.title("Field 3 Chart")

        plt.subplot(3, 2, 4)
        plt.plot(range(0, 100), field_6_degC, 'green')
        plt.axhline(y=mean_field6_degC, color='g', linestyle='--')
        plt.xlabel('date')
        plt.ylabel('Temperature')
        plt.title('Temperature in Celsius')

        plt.subplot(3, 2, 5)
        plt.plot(range(0, 100), field_77, 'magenta')
        plt.axhline(y=mean_field7, color='m', linestyle='--')
        plt.xlabel('date')
        plt.ylabel('Humidity')
        plt.title('Humidity')

        #To prevent overlapping of the graphs
        plt.tight_layout()

        plt.show()
    #In order to continue the reading of new local values all the time, remove the break so that the new set of 100 values
    #are calculated again when the prev. values are finsihed filling the buffer
    break