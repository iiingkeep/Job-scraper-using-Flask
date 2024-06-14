# class: 데이터가 어떻게 생겨야하는지에 대한 청사진으로, 데이터의 구조 정의

# class 생성
class Puppy:
  pass

# 선언: ruffus는 Puppy의 한 종류이다
ruffus = Puppy()

print(ruffus)
'''
=> 출력된 결과를 보면 ruffus가 Puppy 객체라는 것을 알 수 있다.
<__main__.Puppy object at 0x0000018ECDB7FA10>
'''


# class 발전시키기: class 안에 method를 넣어 준다.
# method: class 안에 있는 function. class 밖에 있는 function은 그대로 function이라 한다.
''' 에러로 인해 주석처리
class Puppy2:

  def __init__():
    print('Puppy is born!')

marry = Puppy2()
print(marry)
'''
'''
Puppy2.__init__() takes 0 positional arguments but 1 was given

=> 출력된 결과로 알 수 있는것
1. Puppy2()를 생성한 순간 Python이 자동으로 Puppy2 class 
   안에 있는 __init__() method를 호출함
2. __init()__ method는 1개의 argument가 필요하다
'''


# method에 argument 넣어주기
class Puppy3:

  def __init__(self):
    print(self)
    print("Pyppy is born!")

cheese = Puppy3()
print(cheese)

'''
<__main__.Puppy3 object at 0x0000026FFBDD2890>
Pyppy is born!
<__main__.Puppy3 object at 0x0000026FFBDD2890>

=> 출력된 결과로 알 수 있는것
class 안의 모든 method는 첫 번째 argument로 자기 자신을 참조 
self와 cheese의 출력 결과를 보면 같은 객체를 같은 메모리상에 가짐
첫 번째 argument인 self와 cheese는 동일한 Puppy3 객체를 참조
'''


# method에 데이터 세팅해보기
# method: class 안에 있는 function으로, 항상 첫번째 argument로 그 method 자체인 class를 참조
class Puppy4:

  def __init__(self):
    self.name = "Choco"
    self.age = 0.1
    self.breed = "Beagle"

choco = Puppy4()
print(choco)
print(choco.name)
print(choco.age)
print(choco.breed)
'''
<__main__.Puppy4 object at 0x0000020A18122DD0>
Choco
0.1
Beagle

=> 출력된 결과로 알 수 있는것
choco를 Puppy4 객체로 선언하니 method에서 설정한 값으로 데이터의 속성이 부여된다. 즉,
choco = Puppy4() 라는 코드가 실행되면 python은 __init__을 호출,
def __init__(choco):
  choco.name = 'Choco'
  choco.age = 0.1
  choco.breed = 'Beagle'
로 정의

=> 문제점
다른 강아지 bibi에 대해 같은 클래스 사용 시 속성값이 choco와 같다.
bibi = Puppy4() 코드가 실행시
  bibi.name = 'Choco'
  bibi.age = 0.1
  bibi.breed = 'Beagle'
'''


# method custom: argument에 속성을 추가해 줌으로써 method를 호출할 때 각각의 데이터가 지정한 value로 정의 가능.
# __init__ method: 입력 변수를 설정할 때 사용. 데이터 정의
class Puppy5:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

bibi = Puppy5(
  name = 'Bibi',
  age = 0.3,
  breed = 'Pomeranian'
  )
pung = Puppy5(
  name = 'Pung',
  age =  0.2,
  breed = 'Korean Jindo Dog'
  )
print(bibi.name, bibi.age, bibi.breed)
print(pung.name, pung.age, pung.breed)
'''
Bibi 0.3 Pomeranian
Pung 0.2 Korean Jindo Dog
'''


# __str__ method: 유저에게 객체에 대해 설명하기 위한 문자열 표현으로, str() 함수와 print() 함수를 사용하여 호출하면 __init__으로 정의된 데이터에 접근하여 return값 출력
class Puppy6:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed
  
  def __str__(self):
    return f"{self.breed} puppy named {self.name}"
  
tommy = Puppy6(
  name = 'Tommy',
  age = 0.3,
  breed = 'Pomeranian'
  )
print(tommy)
'''
=> tommy = Puppy6(~~~) 코드가 실행되면 자동으로 __str__ method를 호출하여 return 값 반환

Pomeranian puppy named Tommy
'''


# 정리
'''
Class: 데이터가 어떻게 생겨야하는지에 대한 청사진으로, 데이터의 구조 정의

Instance: class의 청사진을 활용해 만들어진 object로, class의 argument에 따라 value를 설정하여 데이터 구체화
=> ruffus, choco, bibi, pung, tommy

Method: class 안에 있는 function으로, 항상 첫번째 argument로 그 method 자체인 class를 참조
=> __init__(): 객체가 생성될 때 자동으로 호출되는 생성자 메서드. 객체 초기화를 위해 입력 변수를 설정할 때 사용. 데이터 정의
=> __str__ (): 유저에게 객체에 대해 설명하기 위한 문자열 표현으로, str() 함수와 print() 함수를 사용하여 호출하면 __init__으로 정의된 데이터에 접근하여 return값 출력
'''
