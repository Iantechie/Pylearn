#Function product to multiply items in a list of numbers
def product(prod_list):
    result = 1
    for item in prod_list:
        result = result*item
    return result
listp = [10,5]
print(product(listp)) #OUTPUT: 50
