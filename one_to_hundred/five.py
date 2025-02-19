# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

"""
by YjY
"""
D=input()
D=D.split(',')
C=50
H=30
Q=[]
for i in D:
    Q.append( int(( (2 * C * int(i) )/H )**0.5) )

for i in range(0,len(Q)-1):
    print(Q[i],end=',')
print(Q[len(Q)-1])


# by Lbs
import math

C = 50
H = 30
input_val = input()
Q = [str(int(math.sqrt(2 * C * float(item) / H))) for item in input_val.split(',')]
print(','.join(Q))

# by Zc
# TODO