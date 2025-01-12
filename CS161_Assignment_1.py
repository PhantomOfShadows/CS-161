#simple print
print('Welcome to my program!')

print('---------------')

#pet info with f strings
#variables
animal = 'dog'
name = 'Leo'
#should print: I have a dog, his name is Leo.
print(f'I have a {animal}, his name is {name}.')

print('---------------')

#inputs in an f string
name = input('Please enter your name:')
age = int(input('Please enter your age, numbers only:'))
savings = int(input('Please enter your yearly savings, numbers only:'))
#extra variables
A_time = 10 #Age
S_time = 5 #savings
Months = 12
#split up the different parts with /n
print(f'Hello {name}! You are currently {age} years old.\n'
      f'In {A_time} years you will be {age + A_time} years old.\n'
      f'If you save ${savings} a year, in {S_time} years you will have saved ${savings * S_time}.\n'
      f'You are saving roughly ${savings // Months} a month.')

print('---------------')

#seconds in a month
s_m = 60 #seconds in a minute
s_h = s_m * 60 #seconds in an hour
s_d = s_h * 24 #seconds in a day
s_M = s_d * 31 #seconds in a month (January)
print(f'There are {s_M} seconds in the month of January.')

print('---------------')

#how many dozens of eggs do you have
eggs = int(input('How many eggs do you have? Numbers only:'))
dozens = eggs // 12
remainder = eggs % 12
print(f'You have {dozens} dozen eggs and {remainder} egg/s remaining')
