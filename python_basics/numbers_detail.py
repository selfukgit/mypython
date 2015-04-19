#!/usr/bin/python
import random
import math 


print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')


# Select an even number in 100 <= number < 1000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# Select another number in 100 <= number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

# First random number
print "random() : ", random.random()

# Second random number
print "random() : ", random.random()

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
print "Random number with seed 10 : ", random.random()

list = [20, 16, 10, 5];

print("unshuffled list = ",list)

random.shuffle(list)
print "Reshuffled list : ",  list

random.shuffle(list)
print "Reshuffled list : ",  list

print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)

print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)

print "acos(0.64) : ",  math.acos(0.64)
print "acos(0) : ",  math.acos(0)
print "acos(-1) : ",  math.acos(-1)
print "acos(1) : ",  math.acos(1)

print "radians(3) : ",  math.radians(3)
print "radians(-3) : ",  math.radians(-3)
print "radians(0) : ",  math.radians(0)
print "radians(math.pi) : ",  math.radians(math.pi)
print "radians(math.pi/2) : ",  math.radians(math.pi/2)
print "radians(math.pi/4) : ",  math.radians(math.pi/4)

