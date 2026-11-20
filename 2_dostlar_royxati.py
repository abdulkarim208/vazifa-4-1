class Contact:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon

    def update_phone(self, new_phone):
        self.telefon = new_phone

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Telefon: {self.telefon}")


c = Contact('Malika', '901234567')
c.update_phone('931112233')
c.show_info()