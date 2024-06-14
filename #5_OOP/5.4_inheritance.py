# 나만의 method 추가하기
# Magic Method: 파이썬이 지원하는 메소드(__init__ 등)
# Method는 다른 method를 포함할 수 있다.
class Puppy:

  def __init__(self, name, breed):
    self.name = name
    self.age = 0.1
    self.breed = breed

  def __str__(self):
    return f"{self.breed} puppy named {self.name}"
  
  def woof_woof(self):
    print('Woof Woof!')

  def introduce(self):
    self.woof_woof()
    print(f"My name is {self.name} and I am a baby {self.breed}")
    self.woof_woof()

ruffus = Puppy(
  name = 'Ruffus',
  breed = "Beagle",
)

ruffus.introduce()
'''
Woof Woof!
My name is Ruffus and I am a baby Beagle
Woof Woof!
'''

# Inheritance: 코드를 reuse할 수 있어 중복을 줄여주며 class를 조직화한다.
# 예를 들어, GuardDog class를 만든다면 Puppy class와 많은 부분 중복이 발생
'''
class GuardDog:

  def __init__(self, name, breed):
    self.name = name
    self.age = 5
    self.breed = breed

  def rrrrr(self):
    print('stay away!')
'''
# 그럴 때, 두 클래스의 공통이 되는 기본 class를 생성해 상속해준다. 이 클래스는 다른 클래스가 가지는 공통 property들을 포함. => class child_class(parent_class): ~ 
# Dog이라는 parent class 생성 후 Puppy와 GuardDog class에 상속
class Dog:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

class Puppy(Dog):

  def woof_woof(self):
    print('Woof Woof!')

class GuardDog(Dog):

  def rrrrr(self):
    print('stay away!')

bibi = Puppy(
  name = 'Bibi',
  age = 0.1,
  breed = "Beagle",
)
print(bibi.name, bibi.age, bibi.breed)
'''
Bibi 0.1 Beagle
'''

# 자식의 class에 해당 property가 없으면 파이썬은 자동으로 부모 class로 가 property를 찾는다.
# super(): 부모 class의 method를 자식 class에서 호출하는 함수. 일반적으로 부모 class의 메서드를 오버라이드(재정의)할 때 사용. 호출 시 변수의 순서 중요!
class Dog:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

class Puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(name, breed, 0.1)
    self.spoiled = True

  def woof_woof(self):
    print('Woof Woof!')

class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(name, breed, 5)
    self.aggressive = True


  def rrrrr(self):
    print('stay away!')

bibi = Puppy(
  name = 'Bibi',
  breed = "Beagle",
)
argo = GuardDog(
  name = 'Argo',
  breed = "Shepherd",
)

print("bibi:", bibi.name, bibi.breed, bibi.age)
bibi.woof_woof()
print("argo:", argo.name, argo.breed, argo.age)
argo.rrrrr()
'''
bibi: Bibi Beagle 0.1
Woof Woof!
argo: Argo Shepherd 5
stay away!
'''

# 상속을 사용함으로써 코드의 중복을 최소화 하면서도 자식 클래스가 독립적으로 자신만의 속성, 메서드 등을 가질 수 있게 된다.