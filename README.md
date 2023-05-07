# Embedded-Air-Quality-Measurement-System

The PI-Trokli development system was used to implement an embedded system for indicating the Air Quality Index (AQI) based on several environmental measurements provided in Thingspeak channel.
Implemented several python scripts to read values from the cloud channel, to calculate AQI values, gathering local values, saving the calculated values in a new cloud channel, usage of LED Matrix and seven segment display were also implemented based on the value drafted per sequence.

TASKS AND SPECIFICATIONS:-
1) Reading Sensor Cloud Data from Thingspeak (Task1.py)
  Accessing the thingspeak channel
  Decoding the cloud reading by using JSON
  Visualizing PM measurements and mean values
  
2) Local Temperature and Humidity Measurement (Task2.py)
  Getting Temperature and Humidity Readings from Sensor
  Implementation of FIFO data buffer
  Visualizing temperature and humidity measurements and mean values
  
3) AQI Calculation (Task3.py)
  Calculate the AQI for each PM measurement
  Transfer AQI levels to a new cloud channel
  Send a warning E-Mail
  
4) User Interface (Task4.py)
  Selection of measurement value to be visualized
  Display mean values on the seven-segment display (7SD)
  Visualizing the measurements on the Matrix LED Display (MLD) (Task4_2)
 
 Overall program structure:-
  All the task codes were combined in the main.py file which was implemented in such a way that the 
  following elements were executed successfully: 
   The program reads the current cloud data and initializes all arrays at the start-up of the program. 
   The user interface including all local visualizations runs continuously. 
   The two cloud channels for reading data and writing data are updated every 60 seconds. 
   The local measurements from the temperature and humidity sensor are taken every 10 seconds. 
   The AQI calculations and transfer to the thingspeak server are executed every 60 seconds.
