class Pokemon:
    def __init__(self,nombre,tipo,hp, ataques = []):
        self.nombre  = nombre
        self.tipo    = tipo
        self.hp      = hp
        self.ataques = ataques
        
    def desmayado(self):
        return self.hp == 0

    def recibir_daño(self,daño): 
        self.hp -= daño
        if self.hp < 0:
            self.hp = 0
    
    def agregar_ataque(self,ataque):
        self.ataques.push(ataque)

    def obtener_ataque(self,nombre_ataque):
        for ataque in self.ataques:
            if ataque.nombre == nombre_ataque:
                return ataque
    
    def ataques_disponibles(self):
        return self.ataques

    def atacar(self,pokemon_enemigo,nombre_ataque):
        self.obtener_ataque(nombre_ataque).atacarPokemon(pokemon_enemigo)

class AtaquePokemon:
    def __init__(self,nombre,daño):
        self.nombre = nombre
        self.daño = daño

    def atacarPokemon(self, pokemon):
        pokemon.recibir_daño(self.daño)

placaje = AtaquePokemon("Placaje", 30)
hoja = AtaquePokemon("Hoja Afilada", 50)
bulb = Pokemon("Bulbasur", "Planta", 200, [placaje, hoja])
pid = Pokemon("Pidgey", "Normal", 70, [placaje])

bulb.atacar(pid, "Placaje")
pid.atacar(bulb, "Placaje")

print(bulb.hp)
print(pid.hp)

