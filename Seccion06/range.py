valueA = 1
valueB = 5
value = int(input(f"Enter a value between {valueA} and {valueB}"))

insideOfRange = valueA <= value <= valueB

if insideOfRange:
    print(f"The value {value} is inside of the range")
else:
    print(f"The value {value} isn't inside of the range")
