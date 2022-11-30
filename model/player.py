from model.team import Team

class Player():
   def __init__(self, name="", player_id=0, address="", email="", gsm=0, phone=0, role="", team=""):
       self.name = name
       self.player_id = player_id
       self.address = address
       self.email = email
       self.gsm = gsm
       self.phone = phone
       self.role = role
       self.team = team
  
   def __str__(self):
       return f"{self.name}, {self.player_id}, {self.address}, {self.email}, {self.gsm}, {self.phone}, {self.role}, {self.team}"