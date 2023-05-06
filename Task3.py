#Importing the necessary libraries as well as necessary values from other tasks
import time
import thingspeak
import requests
import json
#Importing necessary values from Task1
from Task1 import field_22, field_33

#Updating AQI values to the new thingskpeak channel
while True:
    channel_id = 1841792
    write_key = "3OS38RVKDDGYRAYS"
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)

    #Defining a function to calculate AQI values for PM 2.5
    def PM_2_5_AQI(a):
        AQI = 0

        if 0 <= a <= 12.0:
            AQI = (((50-0)*(a-0))/(12-0)) + 0
        elif 12.1 <= a <= 35.4:
            AQI = (((100-51)*(a-12.1))/(35.4-12.1)) + 51
        elif 35.5 <= a <= 55.4:
            AQI = (((150-101)*(a-35.5))/(55.5-35.5)) + 101
        elif 55.5 <= a <= 150.4:
            AQI = (((200-151)*(a-55.5))/(150.4-55.5)) + 151
        elif 150.5 <= a <= 250.4:
            AQI = (((300-201)*(a-150.5))/(250.4-150.5)) + 201
        elif 250.5 <= a <= 350.4:
            AQI = (((400-301)*(a-250.5))/(350.4-250.5)) + 301
        elif 350.5 <= a <= 500.4:
            AQI = (((500-401)*(a-350.5))/(500.4-350.5)) + 401

        AQI = round(AQI,3)
        return AQI


    # Defining a function to calculate AQI values for PM 10
    def PM_10_AQI(a):
        AQI = 0

        if 0 <= a <= 54.0:
            AQI = (((50-0)*(a-0))/(54-0)) + 0
        elif 55 <= a <= 154:
            AQI = (((100-51)*(a-55))/(154-55)) + 51
        elif 155 <= a <= 254:
            AQI = (((150-101)*(a-155))/(254-155)) + 101
        elif 255 <= a <= 354:
            AQI = (((200-151)*(a-255))/(354-255)) + 151
        elif 355 <= a <= 424:
            AQI = (((300-201)*(a-355))/(424-355)) + 201
        elif 425 <= a <= 504:
            AQI = (((400-301)*(a-425))/(504-425)) + 301
        elif 505 <= a <= 604:
            AQI = (((500-401)*(a-505))/(604-505)) + 401

        AQI = round(AQI,3)
        return AQI

    #Defining empty lists
    AQI_PM_2_5 = []
    AQI_PM_10 = []

    #Storing AQI values in the respective list variables
    for i in field_22:
        j = PM_2_5_AQI(round(i, 1))
        AQI_PM_2_5.append(j)

    for i in field_33:
        j = PM_10_AQI(round(i, 1))
        AQI_PM_10.append(j)

    print((AQI_PM_2_5))
    print(AQI_PM_10)

    #Updating the max values of AQI of PM 2.5 and PM 10 in the respective fields of the created channel
    channel.update({"field4": max(AQI_PM_2_5), "field5": max(AQI_PM_10)})

    k = 0
    #Updating the AQI values of PM 2.5 and 10 in the respective fields of the created channel
    while k < 100:
        channel.update({"field2": AQI_PM_2_5[k], "field3": AQI_PM_10[k]})
        time.sleep(60)
        k = k+1