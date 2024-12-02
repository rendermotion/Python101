# This is how you create a function
def my_amount_of_numbers(amount, name='x_name'):
    for each in range(amount):
        print(name, each)

my_amount_of_numbers(10)
my_amount_of_numbers(5, name='dora')
my_amount_of_numbers(7, name='Jose')

# This is an example of some build in functions
# range()
# print()
# type()
# int()
# str()
# bool()
# float()
# len()
# enumerate()
# reversed()
# zip()
# chr()
# ord()

names = ['Daniel', 'ana', 'Mario', 'husein']
lastnames = ['Ruiz', 'Jackson', 'Wayne', 'Martinez']
import pymel.core as pm
start_number = 65
selection = pm.ls(selection=True)

for offset, each in enumerate(selection):
    print(offset)
    each.rename(f'cube{chr(start_number + offset)}')

for each_name, each_lastname in zip(names, lastnames):
    print(each_name, each_lastname)
print(ord('a'))

