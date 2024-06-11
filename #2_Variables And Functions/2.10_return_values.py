# return: 함수의 바깥으로 값을 보낼 수 있도록 한다. 다른 함수나 변수가 재사용할 수 있다.
# return을 마주하면 함수는 끝이 난다. return 이후에 어떤 코드가 적혀있더라도 실행되지 않는다. 
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print('thank you for paying', tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)
# 위의 두 줄은 다음과 같이 한 줄의 코드로 줄일 수 있다
pay_tax(tax_calc(150000000))


# string 안에 variables 넣기
# f"" 안에 {variable}을 넣어주면 된다.
my_name = 'Judy'
my_age = 22
my_color_eyes = 'brown'

print(f"hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")


# juice function 만들기
def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🧂"

juice = make_juice('🍋')
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)


