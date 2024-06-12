# while 조건문
# while의 조건문이 True일 때 while문 안의 코드를 반복해 메모리를 다 쓸 때까지 실행.
# 조건문이 True일 때 코드를 반복 실행하다 False가 되면 실행을 멈춤

distance = 0
while distance < 20:
  print("I'm running:", distance, "km")
  distance += 1

# while문을 이용한 파이썬 카지노 게임 만들기
# 1~50까지의 숫자 중 랜덤으로 숫자를 골라 컴퓨터가 고른 숫자와 같으면 유저가 이기는 게임. 단, 유저가 숫자를 맞출때까지 반복해서 숫자를 입력할 수 있도록 한다. 유저가 숫자를 맞추면 게임은 끝이난다.
from random import randint

print("Welcome to Python Casino🎲")
pc_choice = randint(1,50)

playing = True

while playing:
  user_choice = int(input("Choose number (1~50):"))
  if user_choice == pc_choice:
    print('You Won!')
    playing = False
  elif user_choice > pc_choice:
    print('Lower!')
  elif user_choice < pc_choice:
    print('Higher!')
