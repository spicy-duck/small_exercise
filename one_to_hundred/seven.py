# Question 13
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# The same letters and the same digits only count once
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 7
# DIGITS 3

output_val = {}
letters_set = set()
numbers_set = set()
input_val = input()
for item in input_val:
    if item.isdigit():
        numbers_set.add(item)
    elif item.isalpha():
        letters_set.add(item)
output_val['LETTERS'] = len(letters_set)
output_val['DIGITS'] = len(numbers_set)
print(output_val)

