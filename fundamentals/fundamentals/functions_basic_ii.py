def countdown(integer):
    return [i for i in range(integer,-1,-1)]

print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([5,3])
print(print_and_return([5,3]))

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]))

def values_greater_than_second(list):
    if len(list) >=2:
        new_list = [i for i in list if i > list[1]]
        print(len(new_list))
        return new_list
    return False

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def this_length_that_value(int1,int2):
    return [int2 for i in range(int1)]

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))