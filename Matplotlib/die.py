#Classe para simular lançamento de dados.

from random import randint

class Die():
    """Uma classe que representa um único dado"""

    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados"""
        self.num_sides = num_sides
    
    def roll(self):
        """Devolve um valor aleatorio entre 1 e o número de dados"""

        return randint(1, self.num_sides) #Devolve entre 1 e 6 (Valor definido no num_sides)
        