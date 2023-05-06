class Enemy:

    def __init__(self,name='Enemy',health=0,hit_power=0):
        self.name = name
        self.health = health
        self.hit_power = hit_power

    def take_damage(self, damage):
        remaining_health = self.health - damage
        if remaining_health > 0:
            self.health = remaining_health
        else:
            self.health = 0
            print("Enemy is dead.")




    def __str__(self):
        return f"Name {self.name}. Health: {self.health}. Hit power: {self.hit_power}"

class Troll(Enemy):


    def take_damage(self,damage):
        super().take_damage(damage)
        if self.health == 0:
            self.health = 100

    def attack(self):
        print(f"Troll attack with power {self.hit_power}")

#troll = Troll()
# troll_with_name = Troll("Troll")
# troll_with_health = Troll("Troll",100)


troll = Troll("Troll", 100, 100)
troll.take_damage(50)
print(troll)
troll.take_damage(50)
print(troll)
troll.take_damage(50)
print(troll)


# print(troll)
# print(troll_with_name)
# print(troll_with_health)
# print(troll_with_power)



# Trolle zawsze 100 życia i 20 ataku HINT: super(). Chcemy miec konstruktor ktory nie przyjmuje parametrow zycia i ataku

#Dopisac kolejnego przeciwnika
#Zawsze ma 200 zycia, ale rozna sila ataku
#Nie bedzie mogl atakowac jezeli jego zycie spadnie ponizej 20 punktow
# Przyjmuje 2 razy mniejsze obrazenia jezeli jego zycie spadnie ponizej 50