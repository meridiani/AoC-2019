###############################################################################
### AoC 2019, Day 2 Part 1

import csv
import sys

###############################################################################
### Constants

### Globals

### Functions

### Replace element in array at location i with value x
def replace_element(array, i, x):
    array[i] = x

### opcode 1: sum to numbers and write the output
def opcode_1(i, j, k, array):
    x = array[i] + array[j]
    replace_element(array, k, x)
    
### opcode 2: sum to numbers and write the output
def opcode_2(i, j, k, array):
    x = array[i] * array[j]
    replace_element(array, k, x)
    
###############################################################################
### Read in file into a list

#with open('test02.txt', 'r') as intcode_file:
with open('input02.txt', 'r') as intcode_file:
    reader       = csv.reader(intcode_file)
    incode_array = list(reader)

data = incode_array[0]
data = [int(i) for i in data]
#data = [1,0,0,0,99]
#data = [2,3,0,3,99]
#data = [2,4,4,5,99,0]
#data = [1,1,1,4,99,5,6,0,99]

###############################################################################
### Replace elements to create the 1202 state
#print(data)
replace_element(data, 1, 12)
replace_element(data, 2, 2)

###############################################################################
### Iterate through array, reading intcode
### Need functions for each opcode 1, 2, 99

#print(data)

for i in range(0,len(data),4):
    value = data[i]
    # check of element is 1, 2 or 99
    if value == 99:
        print('STOP!!!')
        break 
    elif value == 1:
        opcode_1(data[i+1],data[i+2],data[i+3],data)
    elif value == 2:
        opcode_2(data[i+1],data[i+2],data[i+3],data)
    else:
        continue

#print(data)
#test = [3500,9,10,70,2,3,11,0,99,30,40,50]
#test = [2,0,0,0,99]
#test = [2,3,0,6,99]
#test = [2,4,4,5,99,9801]
#test = [30,1,1,4,2,5,6,0,99]

#print(test)
###############################################################################
### Print answer: element 0

print('Answer is: ', data[0])

###############################################################################
print('OK to go!')
