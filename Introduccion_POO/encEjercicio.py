class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta #Atributo protegido
        self.__saldo = saldo #Atributo privado

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        self.__saldo += monto
        
    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

# Modo de uso
cuenta = CuentaBancaria("12345", 1000)
print(cuenta._numero_cuenta)      
#print(cuenta.cuenta.__saldo) #No se puede acceder a un atributo privado


# No es recomendable acceder a los atributos directamente
#print(cuenta.CuentaBancaria.__saldo) #No se puede acceder a un atributo privado

# Se recomienda acceder a los atributos mediante los métodos get y set
valor = cuenta.get_saldo()
print(valor)

# utilizar metodos publicos
cuenta.depositar(500)
cuenta.retirar(2000)
print(cuenta.get_saldo())
cuenta.retirar(500)
print(cuenta.get_saldo())



