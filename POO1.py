class Producto:
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    @property   # getter
    def codigo(self):
        return self._codigo

    @codigo.setter  # setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def calcular_total(self, unidades):
        return self._precio * unidades

    def __str__(self):
        return "Codigo: " + str(self._codigo) + ", Nombre: "  + str(self._nombre) + ", Precio: "  + str(self._precio)

p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Producto 2", 10)
p3 = Producto(3, "Producto 3", 20)

print(p1.calcular_total(10))
print(p3.calcular_total(10))
print(p2.calcular_total(10))
