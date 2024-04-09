#Making your code interactibe by allowing users to add their input

#input() function promprt user with a string, and allows them to respond WITH A STRING

#input() ALWAYS RETURNS A STRING


# food = input("What is your favorite food? ")


# if food == 'tacos':
#     print("We're gonna get along just fine!")
# else:
#     print('WRONG ANSWER')
#     last_words = input('Any last words? ')
#     print("I'll put", last_words, 'on your tomb stone!')

#If you're going to use arithmatic or boolean operators (>,<,>=,<=) I need to convert to int
#since input returns a string, and I need to use an int
age = int(input('How old are you'))

if age >= 65:
    print("you're a senior")
else:
    print("You're just a youngster")