#Importing the necessary values from other tasks
from Task1 import *
from Task2 import *

#Defining a function: (split_fields), to split each field of 100 values into 8 parts
def split_fields(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

#For field1
result_1 =split_fields(field_11, 8)

#Creating empty lists to store array of 8 divided parts
b0 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b = [b0, b1, b2, b3, b4, b5, b6, b7]
#Another empty list to store mean of each individual array
mean_values = []
#for loop for storing values in each empty
for i in range(len(result_1)):
    b[i] = result_1[i]
    #Average is calculated and empty list for mean values is updated
    ch = mean(b[i])
    mean_values.append(ch)
print("mean of eight parts (field_1):", mean_values)
bh_1 = []
#Scaling mean values for the display
for i in range(8):
    b = int(round(6*(mean_values[i]/100)))
    bh_1.append(b)
print('field_1', bh_1)

#Similarly for other fields

#For field2
result_2 =split_fields(field_22, 8)

#Creating empty lists to store array of 8 divided parts
b0 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

b = [b0, b1, b2, b3, b4, b5, b6, b7]

#Another empty list to store mean of each individual array
mean_values = []


#for loop for storing values in each empty
for i in range(len(result_2)):
    b[i] = result_2[i]
    #Average is calculated and empty list for mean values is updated
    ch = mean(b[i])
    mean_values.append(ch)
print("mean of eight parts (field_2):", mean_values)

bh_2 = []

#Scaling mean values for the display
for i in range(8):
    b = int(round(6*(mean_values[i]/100)))
    bh_2.append(b)
print('field_2', bh_2)

#For field3
result_3 =split_fields(field_33, 8)

#Creating empty list to store array of 8 divided parts
b0 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

b = [b0, b1, b2, b3, b4, b5, b6, b7]

#Another empty list to store mean of each individual array
mean_values = []

#for loop for storing values in each empty
for i in range(len(result_3)):
    b[i] = result_3[i]
    #Average is calculated and empty list for mean values is updated
    ch = mean(b[i])
    mean_values.append(ch)
print("mean of eight parts (field_3):", mean_values)

bh_3 = []
#Scaling mean values for the display
for i in range(8):
    b = int(round(6*(mean_values[i]/100)))
    bh_3.append(b)
print('field_3', bh_3)


#For field6

#NOTE: using the values after converting everything into celsius
#Converting deque value into list for splitting purpose
result_temp =split_fields(list(field_6_degC), 8)

#Creating empty list to store array of 8 divided parts
b0 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

b = [b0, b1, b2, b3, b4, b5, b6, b7]

#Another empty list to store mean of each individual array
mean_values = []

#for loop for storing values in each empty
for i in range(len(result_temp)):
    b[i] = result_temp[i]
    #Average is calculated and empty list for mean values is updated
    ch = mean(b[i])
    mean_values.append(ch)
print("mean of eight parts (field_6):", mean_values)

bh_4 = []

#Scaling mean values for the display
for i in range(8):
    b = int(round(6*(mean_values[i]/100)))
    bh_4.append(b)
print('field_6_in_C', bh_4)


#For field7

#Converting deque into list for splitting purpose
result_humidity=split_fields(list(field_77), 8)


#Creating empty list to store array of 8 divided parts
b0 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

b = [b0, b1, b2, b3, b4, b5, b6, b7]

#Another empty list to store mean of each individual array
mean_values = []

#for loop for storing values in each empty
for i in range(len(result_humidity)):
    b[i] = result_temp[i]
    #Average is calculated and empty list for mean values is updated
    ch = mean(b[i])
    mean_values.append(ch)
print("mean of eight parts (field_7):", mean_values)

bh_5 = []
#Scaling mean values for the display
for i in range(8):
    b = int(round(6*(mean_values[i]/100)))
    bh_5.append(b)
print('field_7', bh_5)