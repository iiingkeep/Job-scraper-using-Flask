# if 조건문: condition이 true일 때 아래의 코드를 실행
'''
if condition:
  code
'''

if 10 > 5:
  print('Correct!')


# if..else: 한 가지 조건만을 확인
# else는 조건이 True가 아닐 때 대안만 제공. 써도 되고, 쓰지 않아도 된다. 선택사항
'''
if condition:
  code  => condition이 True일 때 실행
else:
  code  => condition이 False일 때 실행
'''

password_correct = True

if password_correct:
  print('Here is your money')
else:
  print('Wring password')

# if..elif..else
# elif는 다른 여러가지 조건들을 검토할 수 있도록 해 준다.
# True가 나오는 구문 뒤의 조건들은 검토하지 않고 해당 구문의 코드만 실행한 뒤 끝낸다.
# else는 모든 경우가 False일 때 마지막에 실행
'''
if condition:
  code  => if의 condition이 True일 때 실행
elif condition:
  code  => if의 condition이 False, elif의 condition이 True일 때 실행
else:
  code  => 앞이 모든 condition이 False일 때 실행
'''
winner = 10

if winner > 10:
  print('Winner is greater than 10')
elif winner < 10:
  print('Winner is less than 10')
else:
  print('Winner is 10')