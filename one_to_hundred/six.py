# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# by Lbs
output_val = []
input_val = input().split(',')
x_coord = int(input_val[0])
y_coord = int(input_val[1])
for x_item in range(0, x_coord):
    output_val.append([x_item * y_item for y_item in range(0, y_coord)])
print(output_val)