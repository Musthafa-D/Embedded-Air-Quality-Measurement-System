#Importing the necessary libraries as well as necessary values from other tasks
from Task1 import mean_field1
from Task1 import mean_field2
from Task1 import mean_field3
from Task2 import mean_field6_degC
from Task2 import mean_field7
from Task4_2 import *
import RPi.GPIO as RPi
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text
from luma.core.legacy.font import CP437_FONT
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.virtual import viewport
from time import sleep

#Defining serial connection
from Adafruit_LED_Backpack import SevenSegment
serial = spi(port=0, device=1, gpio=noop())
# Define device Max7219
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)

#Creating a new 7 Segment Display instance with the I2C address 0x70
SSD= SevenSegment.SevenSegment(address=0x70)
# Initialise 7SD
SSD.begin()

#Accessing left and right buttons via assigning the respective pin numbers
left = 25
right = 19

#Defining that the GPIO (BCM) numberings system is been used
RPi.setmode(RPi.BCM)

#Setting the pins as imput pins so that the buttons are used as input sources
RPi.setup(left, RPi.IN, pull_up_down=RPi.PUD_OFF)
RPi.setup(right, RPi.IN, pull_up_down=RPi.PUD_OFF)

x = [0, 1, 2, 3, 4]
i = 0
#The loop runs continuosly
while True:
    print("Button is NOT pressed!")
    #Iterate through all elements of the GPIOInputPins array
    while True:
        with canvas(device) as draw:
            draw.line([x[i], 0, x[i], 0], fill="white")
        sleep(0.1)

        if not RPi.input(right):
            i = i + 1
            with canvas(device) as draw:
               draw.line([x[i], 0, x[i], 0], fill="white")
            sleep(0.1)
            print("Right Button is pressed!")
        if not RPi.input(left):
            i = i - 1
            with canvas(device) as draw:
                draw.line([x[i], 0, x[i], 0], fill="white")
            sleep(0.1)
            print("Left Button is pressed!")

        #Setting various cases to display the 7SD and MLD of the respective field values' calculations
        if (i==0):
            StrMeasurement = str(int(10*(round(mean_field1, 1))))
            for j in range(0, len(StrMeasurement)):
                #Allocation of the values that are to be displayed in 7SD are allocated based on their length
                # for right way of display
                if (len(StrMeasurement)==2):
                    SSD.set_digit(j + 2, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
                if (len(StrMeasurement)>=3):
                    SSD.set_digit(j + 1, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
            SSD.write_display()

            #Calling the field1 values from Task4_2 to draw the respective graph
            with canvas(device) as draw:
                for k in range(0, 8):
                    try:
                        draw.point([k, 7 - bh_1[k]], fill="white")
                    except:
                        print("Something went wrong")
                    else:
                        draw.point([k, bh_1[k] - 7], fill="white")

        if (i==1):
            StrMeasurement = str(int(10*(round(mean_field2, 1))))
            for j in range(0, len(StrMeasurement)):
                #Allocation of the values that are to be displayed in 7SD are allocated based on their lenght
                # for right way of display
                if (len(StrMeasurement) == 2):
                    SSD.set_digit(j + 2, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
                if (len(StrMeasurement) >= 3):
                    SSD.set_digit(j + 1, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
            SSD.write_display()

            #Calling the field2 values from Task4_2 to draw the respective graph
            with canvas(device) as draw:
                for k in range(0, 8):
                    try:
                        draw.point([k, 7 - bh_2[k]], fill="white")
                    except:
                        print("Something went wrong")
                    else:
                        draw.point([k, bh_2[k] - 7], fill="white")

        if (i==2):
            StrMeasurement = str(int(10*(round(mean_field3, 1))))
            for j in range(0, len(StrMeasurement)):
                #Allocation of the values that are to be displayed in 7SD are allocated based on their lenght
                # for right way of display
                if (len(StrMeasurement) == 2):
                    SSD.set_digit(j + 2, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
                if (len(StrMeasurement) >= 3):
                    SSD.set_digit(j + 1, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
            SSD.write_display()

            #Calling the field3 values from Task4_2 to draw the respective graph
            with canvas(device) as draw:
                for k in range(0, 8):
                    try:
                        draw.point([k, 7 - bh_3[k]], fill="white")
                    except:
                        print("Something went wrong")
                    else:
                        draw.point([k, bh_3[k] - 7], fill="white")

        if (i==3):
            StrMeasurement = str(int(10*(round(mean_field6_degC, 1))))
            for j in range(0, len(StrMeasurement)):
                #Allocation of the values that are to be displayed in 7SD are allocated based on their lenght
                # for right way of display
                if (len(StrMeasurement) == 2):
                    SSD.set_digit(j + 2, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
                if (len(StrMeasurement) >= 3):
                    SSD.set_digit(j + 1, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
            SSD.write_display()

            #Calling the field6 values from Task4_2 to draw the respective graph
            with canvas(device) as draw:
                for k in range(0, 8):
                    try:
                        draw.point([k, 7 - bh_4[k]], fill="white")
                    except:
                        print("Something went wrong")
                    else:
                        draw.point([k, bh_4[k] - 7], fill="white")

        if (i==4):
            StrMeasurement = str(int(10*(round(mean_field7, 1))))
            for j in range(0, len(StrMeasurement)):
                #Allocation of the values that are to be displayed in 7SD are allocated based on their lenght
                # for right way of display
                if (len(StrMeasurement) == 2):
                    SSD.set_digit(j + 2, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
                if (len(StrMeasurement) >= 3):
                    SSD.set_digit(j + 1, StrMeasurement[j], decimal=False)
                    SSD.set_decimal(2, 1)
            SSD.write_display()

            #Calling the field7 values from Task4_2 to draw the respective graph
            with canvas(device) as draw:
                for k in range(0, 8):
                    try:
                        draw.point([k, 7 - bh_5[k]], fill="white")
                    except:
                        print("Something went wrong")
                    else:
                        draw.point([k, bh_5[k] - 7], fill="white")
