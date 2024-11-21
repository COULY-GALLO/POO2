class Mago:
    def hechizos(self):
        print("El Mago lanza un hechizo.")

class Guerrero:
    def defensa(self):
        print("El Guerrero se defiende .")

class Elfo:
    def aura(self):
        print("El Elfo emite un aura .")

class DarkLord(Guerrero, Elfo):
    def hechizos(self):
        print("El DarkLord lanza un hechizo.")
    
    def ataque(self):
        print("DarkLord hace un ataque.")

dark_lord = DarkLord()
dark_lord.hechizos()
dark_lord.defensa()
dark_lord.aura()
dark_lord.ataque()

print("\nMRO de DarkLord:", DarkLord.__mro__)

class DarkLord2(Elfo, Guerrero):
    def hechizos(self):
        print("DarkLord2 lanza un hechizo .")
    
    def ataque(self):
        print("DarkLord2 hace un ataque.")

dark_lord2 = DarkLord2()
dark_lord2.hechizos()
dark_lord2.defensa()
dark_lord2.aura()
dark_lord2.ataque()

print("\nMRO de DarkLord2:", DarkLord2.__mro__)
