class Ticket:
    def __init__(self, film, narx, soni):
        self.film = film
        self.narx = narx
        self.soni = soni

    def total_cost(self):
        return self.narx * self.soni

    def show_info(self):
        print(f"Film: {self.film}")
        print(f"Umumiy xarajat: {self.total_cost()}")


t = Ticket('Avatar', 40000, 3)

print(t.total_cost())
t.show_info()