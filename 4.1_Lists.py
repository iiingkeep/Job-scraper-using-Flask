# Data structure: 데이터를 구조화하고 싶을 때 사용

# List: []안에 각각의 데이터를 나열
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Index: list 구조에서 특정 위치에 있는 데이터 값 가져올 때 사용
print(days_of_week[0])
'''
Mon
'''

# list에 사용가능한 method
# count method: days_of_week리스트에 다음의 value가 몇개 있는지
print(days_of_week.count('Wed'))
'''
1
'''

# mutate data
# reverse method: 리스트의 value 순서를 반전
days_of_week.reverse()
print(days_of_week)
days_of_week.reverse()
print(days_of_week)
'''
['Fri', 'Thu', 'Wed', 'Tue', 'Mon']
['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
'''
# append method: 리스트에 value 추가
days_of_week.append('Sat')
days_of_week.append('Sun')
print(days_of_week)
'''
['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
'''
# remove method: 리스트의 특정 value 삭제
days_of_week.remove('Mon')
print(days_of_week)
'''
['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
'''
# clear method: 리스트의 모든 value 삭제
days_of_week.clear()
print(days_of_week)
'''
[]
'''