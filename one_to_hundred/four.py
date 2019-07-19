# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class four(object):

    def __init__(self, input_string):
        """
        构造函数
        :param input_string:
        """
        self._input_string = input_string

    @property
    def get_string(self):
        """
        get
        :return:
        """
        return self._input_string

    def print_string(self):
        """
        print
        :return:
        """
        print(self.get_string.upper())

input_string = input()
test_four = four(input_string)
test_four.print_string()


