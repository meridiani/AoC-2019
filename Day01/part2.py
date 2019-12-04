###############################################################################
### Advent of Code 2019, Day 1

import math

### Constants

A = 3.
B = 2.

###############################################################################
### Function to calculate fuel needed for launch
def fuel_for_launch(mass):
    fuel = math.floor((mass/A)) - B
    return fuel

###############################################################################
### Read input file
mass_file = open('input01.txt','r')
#mass_file = open('test01.txt','r')

###############################################################################
### calculate fuel for each mass, in file, iterate until 0 and find the total

total_fuel = 0
for line in mass_file:
    mass = int(line)
    while mass > 0:
        fuel = fuel_for_launch(mass)
        mass = fuel
        if fuel > 0:
            print('fuel is' + str(fuel))

            total_fuel = total_fuel + fuel

print(total_fuel)

###############################################################################
print('OK to go!')    
