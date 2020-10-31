from random import randint

class Die:
    """Crea un dado"""

    def __init__(self, num_sides = 6):
        """Inicializa un dado con 6 caras"""
        self.num_sides = num_sides

    def roll(self):
        """Rueda el dado"""
        return randint(1, self.num_sides)
