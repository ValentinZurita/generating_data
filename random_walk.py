from random import choice

class RandomWalk:
    """Una clase para generar paseos aleatorios"""

    def __init__(self, num_points = 500):
        """Inicializa los atributos del paseo aleatorio"""
        
        # Numero de puntos que se colocaroan en la grafica.
        self.num_points = num_points

        # Todos los paseos comienzan en (0,0).
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calcula todos los puntos en el paseo"""

        # Se dan pasos aleatorios hasta que se cumple el numero deseado.
        while len(self.x_values) < self.num_points:

            # Decidir en que direccion ir y que tan lejos ir en esa direccion.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance # Coordenada x

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance # Coordenada y

            # Rechazar movimientos que no van a ningun lado.
            if x_step == 0 and y_step == 0:
                continue

            # Calcular la nueva posicion.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Agregar las nuevas posiciones al array de pasos.
            self.x_values.append(x)
            self.y_values.append(y)



