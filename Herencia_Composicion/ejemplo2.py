class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

def enviar_correo(self, asunto, mensaje):
    #Logica para enviar correo electronico
    print(f"Correo enviado a {self.email} con asunto {asunto} y mensaje {mensaje}")

def guardar_registro(self, accion):
    #Logica para guardar registro de acciones del usuario
    print(f"Registro guardado: {accion}")

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        usuario.enviar_correo("Bienvenido", "Gracias por registrarte")
        usuario.guardar_registro("Registro de usuario creado")

# Ejemplo de uso
gestor_usuarios = GestorUsuarios()
gestor_usuarios.agregar_usuario("Juan", "juan@example.com")
