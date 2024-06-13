# Tuple: ()안에 데이터 나열. 불변성(Immutable)의 특징을 가진다.
# 즉, 튜플 안의 데이터를 삭제, 수정할 수 없고 데이터 추가도 불가.
# 절대 변하지 않아야 하는 데이터에 대해 사용
# method: index()와 count()만 가능

days = ('Mon','Tue','Wed')
print(days.count('Mon'))
'''
1
'''
print(days[-1])
'''
Wed
'''
