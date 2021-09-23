# Basic calculator from python

num1 = input('Enter 1st Digit: ')
op = input('Enter math operator: ')
num2 = input('Enter 2nd Digit: ')
result = 0.0

if op == '+':
    result = float(num1) + float(num2)
    print('The result of Addition: ', result)
elif op == '-':
    result = float(num1) - float(num2)
    print('The result of Subtraction: ', result)
elif op == '*':
    result = float(num1) * float(num2)
    print('The result of Multiplication: ', result)
elif op == '/':
    result = float(num1) / float(num2)
    print('The result of Division: ', result)
elif op == '%':
    result = float(num1) % float(num2)
    print('The result of Modulo: ', result)
else:
    print('Invalid inputs!')
    
