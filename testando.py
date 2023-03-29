from servivo import SerVivo
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin

# Criação de instâncias das classes
ser_vivo = SerVivo(100, 10)
monstro = Monstro(200, 20, "Monstro Genérico")
lobo = Lobo(150, 15, "Lobo Selvagem", 50)
goblin = Goblin(120, 12, "Goblin Trapaceiro", 80)

# Impressão dos atributos dos objetos criados
print(f"Ser Vivo - Pontos de Vida: {ser_vivo.pontos_de_vida}, Pontos de Ataque: {ser_vivo.pontos_de_ataque}")
print(f"Monstro - Pontos de Vida: {monstro.pontos_de_vida}, Pontos de Ataque: {monstro.pontos_de_ataque}, Tipo: {monstro.tipo}")
print(f"Lobo - Pontos de Vida: {lobo.pontos_de_vida}, Pontos de Ataque: {lobo.pontos_de_ataque}, Tipo: {lobo.tipo}, Força: {lobo.forca}")
print(f"Goblin - Pontos de Vida: {goblin.pontos_de_vida}, Pontos de Ataque: {goblin.pontos_de_ataque}, Tipo: {goblin.tipo}, Inteligência: {goblin.inteligencia}")

