#function sum  for integers and floats
from unittest import result


def sum_(n):
    total = 0
    for item in n:
        total = total + item
    return total
num_list = [10.5,90,100]
print(sum_(num_list)) #OUTPUT: 200.5

#function sum for strings, concatinates given string items in a list
def sum_(str_list):
    result = ''
    for str_item in str_list:
        result = result + str_item
    return result
str = ["Python", "Is", "Cool"]
print(sum_(str)) #OUTPUT: PythonIsCool