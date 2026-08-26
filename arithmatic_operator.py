value1 = int(input("Select value 1: "))
operator = input("Select operator: ")
value2 = int(input("Select value 2: "))

if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "/":
    result = value1 / value2
elif operator == "*":
    result = value1 * value2
elif operator == "%":
    result = value1 % value2
elif operator == "**":
    result = value1 ** value2
else:
    result = operator + " is invalid operator"

print(result)