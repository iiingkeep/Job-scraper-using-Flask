# 문자열은 따옴표로 감싸주어 문자열 데이터로 만들어줘야 함
# 따옴표로 감싸지 않은 문자는 variable로, 앞에서 정의한 적 없다면 에러 발생
# 숫자도 따옴표로 감싸면 문자열 데이터가 된다.
'''
my_name = Ann => 에러
'''
my_name = 'Ann'
my_age = '88'
print(my_name)


# boolean: true(1,on)/false(0,off) 상태를 나타낸다
# True / False 와 같이 첫 글자는 대문자로 표기해야 한다.
'''
dead = true => 대문자로 시작하지 않는 true는 variable로 인식
dead = 'True' => 문자열 True
'''
dead = True
alive = False
print(dead)
print(alive)


print('Hello my name is', my_name)
print("And I'm", my_age, 'years old.')