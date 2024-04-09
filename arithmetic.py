#Math Operations

#Order Operations
#(3+4)+4**2-6/5*4
#PEMDAS (left to right priority)
#Parenthesis
#Exponents
#Multply and Divide tied for Third (left to right priority)
#Addition and Substraction tied for Fourth (left to right priority)




#By default division is the only operation that returns a float
#If you incorporate a float in any other math operation a float will be returned
#Otherwise they will return an int

# Addition use '+'
my_sum = 3 + 5 + 7 + 2.0
print(my_sum)

# Addition assign: reassign the variable to it's current value plus a new value
my_sum += 2
print('Addition Assign:', my_sum)

#Subtraction use '-'

diff = 10 -2
print(diff)

#Subtract assign

diff -= 1
print('Subtract Assign 1:', diff)

#Multiplication use '*' shift+8
prod = 10 * 3
print(prod)

#Multiply assign
prod *= 2
print('Multiply Assign 2:', prod)

#Division using '/' always returns a float
quotient = 10 / 2
print(quotient)

#Division Assign
quotient /= 2
print('Division Assign 2:', quotient)

#Floor Division use '//' (rounds down to nearest whole number)
pre_rounded = 10/7
print(pre_rounded)
rounded = 10//7
print(rounded)

#Floor Divide Assign
x = 30
x //= 4
print('Floor Divide Assign 30 //= 4:', x)

#Modulo use '%' returns the remainder of division
remainder = 32 % 6
print(remainder)

#Modulo Assign
remainder %= 2
print('Modulo Assign 2:', remainder)

#Exponents use '**' (how many times we're going to multiply a number by itself)
square = 5**2
print('Squaring 5:', square)

cubing = 5**3
print('Cubing 5:', cubing)

#Exponent Assign
square **= 2
print(square)