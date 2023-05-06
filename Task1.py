#Importing necessary libraries
import requests
import json
from matplotlib import pyplot as plt
from statistics import mean

#Importing data from thingspeak channel
field_data = requests.get('https://thingspeak.com/channels/628559/feed.json')
fields = json.loads(field_data.text)
feeds = fields["feeds"]

#Defining empty lists for all the 8 fields
field1 = []
field2 = []
field3 = []
field4 = []
field5 = []
field6 = []
field7 = []
field8 = []

#Storing the respective field values in each of the field lists using a for loop
for i in range(0, 100):
    data1 = feeds[i]["field1"]
    field1.append(data1)

    data2 = feeds[i]["field2"]
    field2.append(data2)

    data3 = feeds[i]["field3"]
    field3.append(data3)

    data4 = feeds[i]["field4"]
    field4.append(data4)

    data5 = feeds[i]["field5"]
    field5.append(data5)

    data6 = feeds[i]["field6"]
    field6.append(data6)

    data7 = feeds[i]["field7"]
    field7.append(data7)

    data8 = feeds[i]["field8"]
    field8.append(data8)

#Storing all the 8 field values in another field list to print the respective field data
field_list= [field1, field2, field3, field4, field5, field6, field7, field8]
for j in range (1,9):
    print("Field ",j," data is", field_list[j-1])

#Calculating the mean values of the 1st 3 fields as required
field_11 = list(map(float, field1))
mean_field1 = mean(field_11)
print("Mean value of field1 is", mean_field1)

field_22 = list(map(float, field2))
mean_field2 = mean(field_22)
print("Mean value of field2 is", mean_field2)

field_33 = list(map(float, field3))
mean_field3 = mean(field_33)
print("Mean value of field3 is", mean_field3)

#Plotting the graph for 1st 3 fields i.e. PM1.0, PM2.5 and PM10.0
plt.subplot(3, 1, 1)
plt.plot(range(0, 100), field_11, 'rd-')
plt.axhline(y=mean_field1, color = 'r', linestyle = '--')
plt.xlabel("sample")
plt.ylabel("PM 1.0 (ATM)")
plt.title("Field 1 Chart")

plt.subplot(3, 1, 2)
plt.plot(range(0, 100), field_22, 'ko-')
plt.axhline(y=mean_field2, color = 'black', linestyle = '--')
plt.xlabel("sample")
plt.ylabel("PM 2.5 (ATM)")
plt.title("Field 2 Chart")

plt.subplot(3, 1, 3)
plt.plot(range(0, 100), field_33, 'bo-')
plt.axhline(y=mean_field3, color = 'b', linestyle = '--')
plt.xlabel("sample")
plt.ylabel("PM 10 (ATM)")
plt.title("Field 3 Chart")

#To prevent overlapping of the graphs
plt.tight_layout()

plt.show()
