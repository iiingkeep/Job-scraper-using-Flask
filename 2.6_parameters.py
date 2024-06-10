# 함수가 데이터를 받기 위해서는 ()괄호 안에 variable을 넣는다. 이 variable을 parameter(매개변수)라고 한다.
# 받은 parameter는 그 함수 안에서만 사용 가능
def say_hello(name):
  print('hello', name, 'how are you?')

# 함수로 전달하고 싶은 데이터를 함수 호출 시 ()안에 넣어준다.
# 이 데이터를 argument(인수)라고 한다.
say_hello('Ann')
say_hello('Dana')


# multiple parameters
# parameter와 argument로 주고 받을 데이터의 순서는 동일해야 한다.
def say_hi(user_name, user_age):
  print('hi', user_name)
  print('you are', user_age, 'years old')

say_hi('Andy', 33)