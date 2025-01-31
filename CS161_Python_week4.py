def average(num_1, num_2, num_3):
    """returns the average of 3 numbers

            parameters:
                    num_1 (int): the first number inputted
                    num_2 (int): the second number
                    num_3 (int): the third number

            returns:
                    the average of the 3 numbers
    """
    return (num_1 + num_2 + num_3)/3
print(average(7,5,9))
print(average(6,6,7))

print('----------------------')

print(average(7,5,9))
print(average(6,6,7))
def average(num_1, num_2, num_3):
    """returns the average of 3 numbers

            parameters:
                    num_1 (float/int): the first number inputted
                    num_2 (float/int): the second number
                    num_3 (float/int): the third number

            returns:
                    the average of the 3 numbers
    """
    return (num_1 + num_2 + num_3)/3
#this code would not run because the function had not yet been defined
#(it will when u run it because it is defined in the question above)

print('----------------------')

def average(num_1, num_2, num_3):
    """returns the average of 3 numbers

            parameters:
                    num_1 (int): the first number inputted
                    num_2 (int): the second number
                    num_3 (int): the third number

            returns:
                    the average of the 3 numbers
    """
    return (num_1 + num_2 + num_3)/3
print(average(7,5,9))
print(average(6,6,7))
#print(num_1)
#this code will not run because num_1 does not have a value outside the function
#I made the part that errors into a comment so it wouldn't break the code

print('----------------------')

def human_years(dog_age):
    """returns age of a dog in human years
            parameters:
                    dog_age (int): the age of a dog
            prints:
                    the given age of a dog and its age in human years
    """
    print(f'{dog_age} dog years is equivalent to {24 + (dog_age - 2) * 4} human years.')
human_years(5)
human_years(11)

print('----------------------')

def car_value(c_type, c_price, years):
    """calculates the value of a car

            parameters:
                    c_type (int): the type of car. 1(German, -5%), 2(Japanese, -7%), 3(Italian, +5%)
                        alters percentage of value gained or lost per year
                    c_price (int): the price of the car
                    years (int): the number of years that have passed

            prints:
                    the value of a car based on the given parameters
    """
    if c_type == 1:
        for value in range(years):
            c_price = c_price - (c_price * .05)
        rc_price = round(c_price, 2)
        print(f'The value of this German car will be worth ${rc_price} after {years} years.')
    elif c_type == 2:
        for value in range(years):
            c_price = c_price - (c_price * .07)
        rc_price = round(c_price, 2)
        print(f'The value of this Japanese car will be worth ${rc_price} after {years} years.')
    elif c_type == 3:
        for value in range(years):
            c_price = c_price + (c_price * .05)
        rc_price = round(c_price, 2)
        print(f'The value of this Italian car will be worth ${rc_price} after {years} years.')
car_value(1, 50000, 20)
car_value(2, 50000, 20)
car_value(3, 50000, 20)

print('----------------------')

def calculate_age(age, name):
    '''

            parameters:
                    age (int): the age of a dog
                    name (str): the name of the dog

            prints:
                    the name and age of a dog in human years
    '''
    print(f'Your dog {name} is {24 + (age - 2) * 4} human years old.')
print("Dog's Age Calculator:")
d_name = input("What is your dog's name? ")
d_age = int(input(f"how old is {d_name}? "))
calculate_age(d_age, d_name)

print('----------------------')

def icecream_price(num_scoops):
    '''
    
            parameters:
                    num_scoops (int): the number of icecream scoops 
    
            returns: 
                    the price of the given number of icecream scoops
    '''
    return round(num_scoops * 1.15 + 2.25, 2)
scoops = int(input("Ice Cream Cone Price Calculator:\n"
                   "How many icecream scoops would you like? "))
print(f'A {scoops}-scoop cone will cost ${icecream_price(scoops)}')