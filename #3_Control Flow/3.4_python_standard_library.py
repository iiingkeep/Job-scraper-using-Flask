# 파이썬 카지노 만들기
# 유저는 숫자를 하나 선택하는데, 컴퓨터에 지정된 숫자(50)와 같은 숫자를 선택했다면 이기는 프로그램
user_choice = int(input('Choose number'))
pc_choice = 50

if user_choice == pc_choice:
  print('You won!')
elif user_choice > pc_choice:
  print('Lower!')
elif user_choice < pc_choice:
  print('Higher!')


# 파이썬 카지노 만들기2
# 컴퓨터는 1~50사이에서 랜덤으로 숫자를 선택하고, 유저가 숫자를 선택해 컴퓨터와 같은 숫자를 선택하면 이기는 프로그램
'''
파이썬이 제공하는 기본 라이브러리 중 random.randint(a,b) 사용
random.randint(a,b): a이상 b이하의 정수 중 무작위 숫자 추출
import하기: from module import function
=> from random import randint
'''
from random import randint

user_choice2 = int(input('Choose number'))
pc_choice2 = randint(1,50)

if user_choice2 == pc_choice2:
  print('You won!')
elif user_choice2 > pc_choice2:
  print('Lower! Computer chose', pc_choice2)
elif user_choice2 < pc_choice2:
  print('Higher! Computer chose', pc_choice2)