class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya -= amount

        if self.energiya < 0:
            self.energiya = 0

    def show_status(self):
        print(f"Oyinchi: {self.ism}")
        print(f"Energiya: {self.energiya}")


p = Player('Hero')
p.use_energy(35)
p.show_status()