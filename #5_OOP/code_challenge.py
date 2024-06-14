# Player와 Team class를 생성
class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
    
  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)


red_team = Team('Team Red')
red_team.add_player('Kelly')
blue_team = Team('Team Blue')
blue_team.add_player('Eden')

print(red_team.players)
'''
[<__main__.Player object at 0x000001A51A613310>]
'''
red_team.show_players()
'''
Hello! I'm Kelly and I play for Team Red
'''


# ✨Code Challenge!✨
# 1. Team class에서 player를 삭제하는 method 만들기.
# 2. Team class에 팀의 경험치(xp) 총합을 보여주는 method 만들기
class Player:

  def __init__(self, name, xp, team):
    self.name = name
    self.xp = xp
    self.team = team

  def introduce(self):
    print(f"Hello! I'm {self.name} and I play for {self.team}. My xp is {self.xp}.")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self):
    for player in self.players:
      player.introduce()

  # Challenge Number 1
  def total_amount_of_team_xp(self):
    total_xp = 0
    for player in self.players:
      total_xp += player.xp
    print(f"Total xp of {self.team_name}: {total_xp}" )

  def add_player(self, name, xp):
    new_player = Player(name, xp, self.team_name)
    self.players.append(new_player)
    print(f"{name} has been added to the {self.team_name}")

  # Challenge Number 2
  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        print(f"{player.name} left {self.team_name}")

team_blue = Team('Team Blue💙')
team_blue.add_player('Sora', 1000)
team_blue.add_player('Jenni', 2000)
team_blue.show_players()
team_blue.total_amount_of_team_xp()
team_blue.remove_player('Sora')
team_blue.show_players()
team_blue.total_amount_of_team_xp()
'''
Sora has been added to the Team Blue💙
Jenni has been added to the Team Blue💙
Hello! I'm Sora and I play for Team Blue💙. My xp is 1000.
Hello! I'm Jenni and I play for Team Blue💙. My xp is 2000.
Total xp of Team Blue💙: 3000
Sora left Team Blue💙
Hello! I'm Jenni and I play for Team Blue💙. My xp is 2000.
Total xp of Team Blue💙: 2000
'''

team_red = Team('Team Red❤️')
team_red.add_player('Jisoo', 1000)
team_red.add_player('Ari', 3000)
team_red.add_player('Yun', 1000)
team_red.show_players()
team_red.total_amount_of_team_xp()
team_red.remove_player('Ari')
team_red.remove_player('Yun')
team_red.show_players()
team_red.total_amount_of_team_xp()
'''
Jisoo has been added to the Team Red❤️
Ari has been added to the Team Red❤️
Yun has been added to the Team Red❤️
Hello! I'm Jisoo and I play for Team Red❤️. My xp is 1000.  
Hello! I'm Ari and I play for Team Red❤️. My xp is 3000.    
Hello! I'm Yun and I play for Team Red❤️. My xp is 1000.    
Total xp of Team Red❤️: 5000
Ari left Team Red❤️
Yun left Team Red❤️
Hello! I'm Jisoo and I play for Team Red❤️. My xp is 1000.  
Total xp of Team Red❤️: 1000
'''

    