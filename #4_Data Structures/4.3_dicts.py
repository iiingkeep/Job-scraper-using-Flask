# Dictionary: {}안에 key - value pair로 이루어진 데이터 존재.
# 여러개의 다른 속성을 가지는 데이터를 구조화할 때 사용

player = {
  'name': 'Ann',
  'age': 22,
  'alive': True,
  'fav-food': ['🍕']
}

# dictionary에 key와 value 추가
player['cute'] = [True]
print(player)
'''
{'name': 'Ann', 'age': 22, 'alive': True, 'fav-food': ['🍕'], 'cute': [True]}
'''
# value가 list인 key에 데이터 추가하기
player['fav-food'].append('🍜')
print(player)
'''
{'name': 'Ann', 'age': 22, 'alive': True, 'fav-food': ['🍕', '🍜'], 'cute': [True]}
'''

# Dictionary method
# get(): key를 입력하면 그에 해당하는 value를 반환
# print(player['age'])로도 가능
print(player.get('age'))
print(player.get('fav-food'))
print(player['age'])
'''
22
['🍕', '🍜']
22
'''
# pop: key를 입력하여 그 key와 value를 삭제
player.pop('fav-food')
print(player)
'''
{'name': 'Ann', 'age': 22, 'alive': True, 'cute': [True]}
'''
