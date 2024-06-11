# default parameter
# 함수에 parameter를 설정해놨지만 함수를 호출할 때 유저가 아무런 argument를 보내지 않는다면 에러가 난다. 이는 유저 경험에 좋지 않으므로 argument가 없어도 에러가 나지 않도록 default 값 설정
# parameter=data
def say_hello(user_name='anonymous'):
  print('hello', user_name)

say_hello('Dani')
say_hello()


# 계산 기능을 하는 함수 만들어보기
# 목표: 유저가 argument를 입력하지 않아도 에러가 나지 않도록 하기

def plus(a=0, b=0):
  print(a + b)
def minus(a=0, b=0):
  print(a - b)
def multiple(a=0, b=0):
  print(a * b)
def power(a=0, b=0):
  print(a ** b)
def divide(a=0, b=1):
  print(a / b)

plus()
minus()
multiple()
power()
divide()
