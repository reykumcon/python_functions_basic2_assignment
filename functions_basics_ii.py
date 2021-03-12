# Countdown

countList = []

def countdown(num):
    for x in range(num, -1, -1):
        countList.append(x)
    return countList

print(countdown(5))

# Print and Return

def print_and_return(list_item):
    num1 = list_item[0]
    num2 = list_item[1]
    print(num1)
    return num2

print(print_and_return([1,2]))

# First Plus Length

def first_plus_length(list_item):
    return list_item[0] + len(list_item)

print(first_plus_length([1,2,3,4,5]))

# Values Greater

def values_greater_than_second(list_item):
    newList = []
    
    for x in range(len(list_item)):
        if len(list_item) < 2:
            return False
        else:
            if list_item[x] > list_item[1]:
                newList.append(list_item[x])
    
    print(len(newList))
    return newList

print(values_greater_than_second([3]))
print(values_greater_than_second([5,2,3,2,1,4]))

# This Length, That Value

def length_and_value(size, value):
    list_item = []
    while(len(list_item) < size):
        list_item.append(value)
    return list_item

print(length_and_value(4,7))
print(length_and_value(6,2))