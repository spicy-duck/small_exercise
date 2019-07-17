#Question:
#With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.

def getdic(ceiling=1):
    if (ceiling >= 1):
        dic = {}
        for index in range(1, ceiling + 1):
            dic[index] = index * index
        print(dic)
    else:
        raise Exception("argements can't less than 1")
getdic(0)
