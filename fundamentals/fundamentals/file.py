num1 = 42 #variable declaration, initialize number
num2 = 2.3
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, initialize tuples
print(type(fruit)) #type check of fruit variable
print(pizza_toppings[1]) #access value of index 1 in list
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #access value in dictionary
person['name'] = 'George' #change value in dictionary
person['eye_color'] = 'blue' #add value to dictionary
print(fruit[2]) #access value of index 2 in list

if num1 > 45: #if conditional
    print("It's greater")
else: #else conditional
    print("It's lower")

if len(string) < 5: #if conditional with len function
    print("It's a short word!")
elif len(string) > 15: #elif conditional with len function
    print("It's a long word!")
else: #else conditional
    print("Just right!")

for x in range(5): #for loop with x = 0 - 4
    print(x)
for x in range(2,5): #for loop with x = 2 - 4
    print(x)
for x in range(2,10,3): #for loop with x = 2 - 8, increment by 3
    print(x)
x = 0 #assign value of 0 to variable x
while(x < 5): #while loop that starts at x = 5, increments by 1 after each loop, and stops when x = 5
    print(x)
    x += 1

pizza_toppings.pop() #delete last value of pizza toppings list
pizza_toppings.pop(1) #delete value index 1 from pizza toppings list
person.pop('eye_color') #delete eye color entry in person dictionary

for topping in pizza_toppings: #for loop that increment throught he pizza toppings list
    if topping == 'Pepperoni': #conditional that checks if list element is equal to string
        continue #return control to for loop
    print('After 1st if statement') #print statement
    if topping == 'Olives': #conditional that checks if list element is equal to string
        break #break loop

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop that iterates through range of numbers
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x): #function declaration
    for num in range(x): #for loop that iterates through range of numbers ending with argument passed to parameter x
        print('Hello') #print statement

print_hello_x_times(4) #function call with 4 passed as argument

def print_hello_x_or_ten_times(x = 10): #function declaration
    for num in range(x): #for loop that iterates through range of numbers ending with argument passed to parameter x. Default value of x = 10
        print('Hello') #print statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call with 4 passed as argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)