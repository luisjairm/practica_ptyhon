"""
    Crea una calculadora simple utilizando clases en Python.
    La calculadora debe ser capaz de realizar operaciones básicas como suma, resta, multiplicación y división.

"""
class Calculadora:
    def suma(self, val_1, val_2):
        res = val_1 + val_2
        return f"{val_1} + {val_2} = {res}"

    def resta(self, val_1, val_2):
        res = val_1 - val_2
        return f"{val_1} - {val_2} = {res}"

    def division(self, val_1, val_2):
        res = val_1 / val_2
        return f"{val_1} / {val_2} = {res}"

    def multiplicacion(self, val_1, val_2):
        res = val_1 * val_2
        return f"{val_1} * {val_2} = {res}"


calc = Calculadora()
suma = calc.suma(20, 2)
resta = calc.resta(25, 2)
div = calc.division(30, 5)
multi = calc.multiplicacion(4,5)


print(suma)
print(resta)
print(div)
print(multi)