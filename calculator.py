

operator = input("enter an operator (+ - * /) : ")
number1 = float(input("enter 1'st number = "))
number2 = float(input("enter 2'nd number = "))

if operator == '+' : 
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)
elif operator == '*':
    result = number1 * number2
    print(result)
elif operator == '/':
    result = number1/number2
    print(result)
else:
    print("is not valid operator")
    
