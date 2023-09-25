"""_summary_
"""

class Coche:
    """_summary_
    """
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")

    def apagar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "se ha apagado")


laguna = Coche("Renault", "Laguna")
tesla = Coche("Tesla", "Model 3")


print(type(laguna))
print(type(tesla))

print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)

tesla.arrancar()
laguna.arrancar()


tesla.apagar()
laguna.apagar()