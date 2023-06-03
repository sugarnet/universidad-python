myVar = int(input("Give me  number: "))

print(f'The number is {myVar}')
print(f'{myVar} % 2 = {myVar%2}')

if myVar % 2 == 0:
    print("The number is pair")
else:
    print("The number is odd")
