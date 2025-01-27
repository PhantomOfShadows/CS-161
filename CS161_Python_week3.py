#get an input and print it
name = input('What is your name? ')
print('Hello', name)

print('-------------------')

#get an integer input, add 5, and print result
#If you don't add int() to the input you'll have characters and not a number.
age = int(input('How old are you? ')) #int(input())
print('In 5 years you will be', age + 5, 'years old')

print('-------------------')

#use str() to turn a number into a string, then print
#gives your age in x number of years, using age from previous input
time = int(input('how many years do you want to add to your age? '))
new_age = str(age + time)
print(f'In {time} years you will be', new_age, 'years old')

print('-------------------')

#calculate how much a person makes in a given number of hours based on hourly wage, using float()
hrs = float(input('Enter number of hours worked in a week: '))
wage = float(input('Enter your hourly wage: $'))
total = round(wage * hrs, 2)
print(f'You make roughly ${total} in a week')
