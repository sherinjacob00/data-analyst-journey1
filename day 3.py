#STRING BASICS

name = 'data analyst'
print(name.upper())
goal = 'i will work at google'
print(goal.replace('google','microsoft'))
city =  'banglore'
print(f'i live in {city}')
text =  'hello world'
print(text[2:8])
age =  20
print(f'my age is {age}')
pet =  'dog'
print(f'i have a pet {pet}')
gadget = "laptop"
print(f'i use my {gadget} to study ')


# IF ELIF ELSE CONDITIONAL STATEMENTS
EG 1 FOOD RESPONSE
response = input('do you like food(Y/N) :')
if response == 'Y':
     print('you have food to eat!')
else :
  print('you have no food here')


# EG 2 AGE

age = float(input('enter your age:'))
if age > 18:
  print('you are eligible to vote')
elif age < 18:
  print('you are not eligible to vote')
else:
  print('congrats for your first vote')

# EG 3 NOT LEAVING AN BLANK INPUT

name = input('enter your name')
if name == '':
  print('not input recived')
else:
  print('input entered successfully')


# # EG 4 BOOLEAN
is_student = False
if is_student:
  print('you are a student')

else:
  print('you are not a student')


# EXERSICE 1 - CALCULATER
operater =  input('enter a operater(+,-,*,/): ')
num1 = float(input('enter first number: '))
num2 = float(input('enter  second number: '))
if operater == '+':
  result = num1 + num2
  print(result)
if operater == '-':
  result = num1 - num2
  print(result)
if operater == '*':
  result = num1 * num2
  print(round(result,3))

if operater == '/':
  result = num1 / num2
  print(round(result,3))
