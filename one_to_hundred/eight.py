# Question 17
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# lbs
ADD = 'D'
DISCOUNT = 'W'
output_val = 0
while True:
    input_val = input()
    if not input_val:
        break
    operates = input_val.split(' ')
    operate_action = operates[0]
    operate_number = int(operates[1])
    if operate_action == ADD:
        output_val += operate_number
    elif operate_action == DISCOUNT:
        output_val -= operate_number
    else:
        pass
print(output_val)