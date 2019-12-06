###############################################################################
### AoC 2019, Day 2 Part 2

import csv
import sys

###############################################################################
### Constants
OUTPUT = 19690720
#OUTPUT = 6087827
STEP   = 4

### find values of noun and verb that produce output

### Globals

### Functions

### Replace element in array at location i with value x
def replace_element(array, i, x):
    array[i] = x

### opcode 1: sum to numbers and write the output
def opcode_1(i, j, k, array):
    #print l m n
    x = array[i] + array[j]
    replace_element(array, k, x)
    
### opcode 2: sum to numbers and write the output
def opcode_2(i, j, k, array):
    x = array[i] * array[j]
    replace_element(array, k, x)

### computer!    
def compute_code(array, noun, verb, step):
    replace_element(array, 1, noun)
    replace_element(array, 2, verb)

    for k in range(0,len(array) - step, step):
        opcode = array[k]
        l      = array[k+1]    
        m      = array[k+2]
        n      = array[k+3]

         # check of element is 1, 2 or 99
        if opcode == 99:
            #print('STOP!!!')
            break 
        elif opcode == 1:
            opcode_1(l,m,n,array)

        elif opcode == 2:
            opcode_2(l,m,n,array)
        else:
            continue

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
orig = list(data)

###############################################################################
### Iterate through array, reading intcode
### Need functions for each opcode 1, 2, 99

### first, does it work like before?

#while data[0] != OUTPUT:
for i in range(100):
    for j in range(100):
        #print(i,j)

        compute_code(data, i, j, STEP)

        answer = data[0]
        noun   = i
        verb   = j

        if answer == OUTPUT:
            print('found it!')
            print(100 * noun + verb)
            break

        data = list(orig)



#compute_code(data, 12, 2, STEP, orig)

#print('After function')
#print(data[0],orig[0])

#noun = 0
#verb = 0


#while data[0] != OUTPUT:
#for i in range(0,100):
#    for j in range(0,100):


### does data[0] == OUTPUT? If yes then stop!
### iterate over data in 4s
### at each one iterate between 0 - 99 the i + 1 and i + 2
### does i + 3 = 0?
### find noun and verb

#print(data)
#test = [30,1,1,4,2,5,6,0,99]

#print(test)
###############################################################################
### Print answer: 100 * noun + verb

#noun = 12
#verb = 2

#print('Answer is: ', 100 * noun + verb)

###############################################################################
print('OK to go!')
