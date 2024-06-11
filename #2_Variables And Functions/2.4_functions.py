# function: 재사용할 수 있는 코드 조각


# print(): 받은 값을 콘솔에 출력
print(True)
print('hello')
print(21)

# function 정의하기
# def: 파이썬에서 function을 정의할 때 앞에 붙여준다.
# 함수의 이름은 공백 사용X, 숫자 또는 특수문자로 시작X
# 함수를 호출하면 실행할 코드는 탭 1번 또는 스페이스바 2번으로 정의한 함수 안으로 들여쓰기 해준다.
def say_hello():
  print('hello how r u?')

def say_bye():
  print('bye bye')

# function 호출하기
# function이름() 의 형태로 함수가 실행될 수 있도록 한다.
# (): function 안의 코드를 실행
say_hello()
