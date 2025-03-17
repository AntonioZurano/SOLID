class Empleados():
    numero_empleados = 0 #atributo de clase

    # Creación del método constructor
    # nombre, cargo y salario --> atributos de instancia
    def __init__(self, nombre, cargo, salario):
        # DATOS ///////////////////////////////////////////////////////////////////////////////////////////
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleados.numero_empleados += 1
            # Incrementar el contador de empleados cuando un empleado se registre
    
        # COMPORTAMIENTO ///////////////////////////////////////////////////////////////////////////////////
    def presentarse (self): # Método de instancia
        print(f"Hola, soy {self.nombre} y ocupo el cargo de {self.cargo}.")
    
    def aumentar_salario(self, porcentaje): #metodo de instancia
        self.salario *= 1 + porcentaje/100
        print(f"Nuevo salario de { self .nombre }: { self .salario }")
    @classmethod    
    def desde_string(cls, datos_empleados): # metodo de una clase
        nombre, cargo, salario = datos_empleados.split(",")
        return cls(nombre, cargo, float(salario))
    @staticmethod
    def es_feriado(dia):
        feriados = [1,10,27]
        return dia in feriados
    
# INSTANCIAR UNA CLASE - CREAR OBJETOS
#Utilizar el metodo de instancia
empleado1 = Empleados("Juan Perez", "Gerente", 5000)
empleado2 = Empleados("Ana Lopez", "Desarrollador", 3000)
empleado5 = Empleados("Adamari Lopez", "Desarrollador2", 3000)

#Utilizar el metodo de clase
empleado3 = Empleados.desde_string("Carlos, Analista, 4000")

# Utilizar los metodos estaticos
print(Empleados.es_feriado(10))

# Acceder al atributo de clase
print(Empleados.numero_empleados)

'''print(empleado3.nombre)
print(empleado3.cargo)
print(empleado3.salario)
print(Empleados.numero_empleados)'''


# LLAMAR A LOS MÉTODOS DE INSTANCIA
#empleado1.presentarse()
#empleado1.aumentar_salario(10)

#empleado2.presentarse()
#empleado2.aumentar_salario(5)

#empleado3.presentarse()