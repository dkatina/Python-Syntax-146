#Indentation is how we define new blocks of code in python 

#if statements check conditions/assertions, and if they are true
#they will run their own code block, if not, that code block won't run

age = 8

if age >= 65:
    print('You are a senior citizen!')


food = 'tacos'

if food == 'Tacos':
    print("Thats what I'm talkin' about!")
else:
    print('IM GONNA THROW A FIT')
#When you are done with a block, unindent

#bad indentation leads to errors, only indent when you need a new block
name = 'Dylan'
    dog = 'Rhiannon'
print(name, 'loves', dog)

