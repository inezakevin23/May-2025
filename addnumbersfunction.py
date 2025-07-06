def calculator(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "error! denominator must be different from 0"
        else:
            return a / b
    else:
        return "error! you entered wrong operator"
a=float(input("Enter first number: "))
operator=input("Enter operator: ")
b=float(input("Enter second number: "))
result=calculator(a,b,operator)
print('your result', result)
