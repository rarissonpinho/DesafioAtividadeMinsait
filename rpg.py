class SerVivo:  
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque


class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo

class Lobo(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, forca):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.forca = forca

class Goblin(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, inteligencia):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.inteligencia = inteligencia

