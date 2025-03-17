# Atributos privados
# class Ejemplo:
#    def __init__(self):
#        self.__atributo_privado = "Carla"

#    def get_atributo(self):
#        print(f"El nombre puede ser tatiana o {self.__atributo_privado}")

#    valor = ejemplo()
    #print(valor.__atributo_privado)
#    valor.get_atributo() #Nosotros controlamos como se muestra un valor privado mediante un metodo publico get

    # Atributos protegidos
class Ejemplo:
    def __init__(self):
        self._atributo_protegido = 20

    def get_atributo(self):
        print(f"El nombre puede ser tatiana o {self._atributo_protegido}")


valor = Ejemplo()
print(valor._atributo_protegido) #no es correcto pero se puede
valor.get_atributo() #Nosotros controlamos como se muestra un valor protegido mediante un metodo publico get

