# input(): 사용자의 응답을 받아야 실행이 끝난다. 
# input함수로 인해 반환되는 데이터는 항상 str.

# age의 타입은 str
age = input('How old are you?')
print('user answer', age)
print(type(age))

# age_number의 타입은 int
age_number = int(input('How old are you?'))
print('user answer', age_number)
print(type(age_number))


# and 와 or
'''
True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False
'''
user_age = int(input('How old are you?'))
if user_age < 18:
  print("You can't drink")
elif user_age >= 18 and user_age <= 35:
  print('You drink beer!')
elif user_age >=36 and user_age <= 80:
  print('You should drink less than before.')
elif user_age == 100 or user_age == 101:
  print('Do what you want to do!')
else:
  print('Go ahead!')