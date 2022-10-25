class Usuarios:
    tipo_usuario = "Free"
    publicidad = True

    def __init__(self,nid,alias,nombre,apellido,*args):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellido = apellido
        self.args = args

usuario1 = Usuarios("001","PdePython","Marcos","Bravo","Persona amante de la programacion")
print(usuario1.args)

class UsuariosPremium(Usuarios):
    tipo_usuario = "Premium"
    publicidad = False

usuario2 = Usuarios("002","PdePython","Paula","Bravo")
print(usuario2.nombre)