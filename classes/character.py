class Character:
    def __init__(self, name, maxhp, hp, atk):
        self.name = name
        self.maxhp = int(maxhp)
        self.hp = int(hp)    # current health
        self.atk = int(atk)  # attack modifiers

    def __str__(self):
        return self.name + "'s HP is " + str(self.hp) + "/" + str(self.maxhp) + " & ATK is " + str(self.atk)

    def take_damage(self, damage):
        self.hp = self.hp - int(damage)
        if self.hp < 0:
            self.hp = 0

    def get_healed(self, healing):
        self.hp = self.hp + int(healing)
        if self.maxhp < self.hp:
            self.hp = self.maxhp

