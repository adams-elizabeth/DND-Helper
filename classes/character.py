class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = int(hp)    # current health
        self.atk = int(atk)  # attack modifiers

    def get_name(self):
        return self.name

    def get_hp(self):
        return str(self.hp)

    def get_atk(self):
        return str(self.atk)

    def take_damage(self, damage):
        self.hp = self.hp - int(damage)
        if self.hp < 0:
            self.hp = 0

    def get_healed(self, healing):
        self.hp = self.hp + int(healing)

