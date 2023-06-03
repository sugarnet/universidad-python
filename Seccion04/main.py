# boolean type
x = True
print(x)
print(type(x))  # type() give us the variable's type

print()

x = False
print(x)
print(type(x))

print()

# int type
x = 10
print(x)
print(type(x))

print()

# float type
x = 10.6
print(x)
print(type(x))

# string type
print()
x = 'Diego'
print(x)
print(type(x))

# string type
print()
x = "Diego"
print(x)
print(type(x))

myBandName = 'Soda Stereo'
comment = 'Is the best band'
# print('My favourite band is: ' + myBandName + ' ' + comment)
print('My favourite band is:', myBandName, comment)

print()
# string concat
number1 = "1"
number2 = "2"
print(number1 + number2)

print()
# int sum
number1 = 1
number2 = 2
print(number1 + number2)

print()
# error
number1 = "1"
number2 = 2
# print(number1 + number2)

print()
# int sum
number1 = "1"
number2 = "2"
print(int(number1) + int(number2))

# boolean type
print()
booleanVar = 1 > 2
if booleanVar:
    print("Was true")
else:
    print("Was false")

# input function
# print()
# inputVar = input("Give me some value: ")
# print("The value was:", inputVar)
# print("This is the end")

# print()
# number1 = int(input("Give me a number: "))
# number2 = int(input("Give me another number: "))
# print("The sum is:", number1 + number2)

# print()
# number1 = int(input("How was your day? (1 - 10) "))
# print("Your day was:", number1)

print()
title = input("What is the book´s name?: ")
author = input("What is the book's author?: ")
# print("The book " + title + " was written by " + author)
print("The book", title, "was written by", author)
