"""
    Crea una clase llamada Empleado que tenga los siguientes atributos:

nombre: El nombre del empleado.
apellido: El apellido del empleado.
salario: El salario base del empleado.
La clase también debe tener los siguientes métodos:

obtener_nombre_completo(): Este método debe devolver el nombre completo del empleado en el formato "nombre apellido".
calcular_salario_anual(): Este método debe devolver el salario anual del empleado. Considera que un año tiene 12 meses.
aumentar_salario(porcentaje): Este método debe aumentar el salario del empleado en el porcentaje dado.
Luego, crea una subclase llamada Gerente que herede de la clase Empleado. La subclase Gerente debe tener un atributo adicional:

bono: El bono anual que recibe el gerente.
La subclase Gerente también debe tener un método adicional:

calcular_salario_anual(): Este método debe calcular el salario anual del gerente teniendo en cuenta el bono.
"""

class  EmployeeManagement:
    def __init__(self, name, last_name, salary):
        self._name = name
        self._last_name = last_name
        self._salary = salary

    def get_full_name(self):
        return f"Nombre Completo: {self._name} {self._last_name}"

    def calculate_annual_salary(self):
        salary = self._salary * 12
        return salary

    def increase_salary(self, value):
        increment = self._salary * (value / 100)
        res = self._salary + increment
        self._salary = res
        return f"El nuevo sueldo de {self._name} es de {self._salary}  "


class Manager(EmployeeManagement):
    def __init__(self, name, last_name, salary, bond):
        super().__init__(name, last_name, salary)
        self._bond = bond

    def calculate_annual_salary(self):
        return super().calculate_annual_salary() + self._bond


empleado1 = EmployeeManagement("Luis Jair", "Mulato Zapo", 100)
gerente = Manager("Enrique", "mulato", 100, 50)

print(empleado1.get_full_name())
print(empleado1.calculate_annual_salary())
print(empleado1.increase_salary(10))
print()
print(gerente.calculate_annual_salary())