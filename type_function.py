#Type function allows us to see the datatype of any given value

print(type('hello world'))
print(type(4))
print(type(3.14))

print(type('123 fun street'))


#Type casting using int() converst qualifying data to an int datatype
x = '4'
print(type(x))

x = int(x)
print(type(x))
print(x)

#Type casting float() to convert qualifying data into a float datatype
x = float(x)
print(type(x))
print(x)

pi = 3.14
print(pi)

#converting to int always rounds down
ball_park = int(pi)
print(ball_park)

#------ Get a valueError because we tryed to convert non-qualifying data
# num = 'four'
# int_num = int(num)
# print(int_num)