"""
Crea un juego de adivinanzas donde la computadora elige un número aleatorio y el jugador tiene que adivinarlo.
La computadora proporcionará pistas para ayudar al jugador a acertar.

"""

import random


class GuessingGame:
    def __init__(self):
        self._random_num = self._generate_random_num()

    @staticmethod
    def _generate_random_num():
        return random.randint(1, 10)

    def get_num(self):
        return self._random_num

    def validate_num(self, value):
        if value < self._random_num:
            return "Mas alto"
        if value > self._random_num:
            return "Mas bajo"


game = GuessingGame()

random_num = game.get_num()

print("Elige un numero entre el 1 y el 10")
while True:
    # print(random_num)
    print("---------------------")
    num = int(input("Ingresa un numero: "))

    if num == random_num:
        print("Correcto")
        break
    else:
        print(game.validate_num(num))
        print("Intenelo de nuevo")
