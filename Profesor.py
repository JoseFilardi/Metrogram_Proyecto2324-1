from User import User

class Profesor(User):
    """
    Clase que representa a un profesor, heredada de la clase User.

    Atributos:
        departamento (string): El departamento al que pertenece el profesor.
        id (string): Identificación única del profesor.
        firstname (string): Nombre del profesor.
        lastname (string): Apellido del profesor.
        username (string): Nombre del profesor en el programa.
        email (string): Correo electrónico del profesor.
        seguidores (list): Lista de seguidores.
        tipo (string): Tipo de usuario 'profesor'.

    Metodos:
        __init__(self, id, firstname, lastname, username, email, departamento, seguidores, tipo):
            Inicializa la instancia de la clase Profesor.

        show_teacher(self):
            Muestra la información del profesor en la consola.
    """
    def __init__(self, id, firstname, lastname, username, email, departamento, seguidores, tipo):
        """
        Inicializa la instancia de la clase Profesor.

        Argumentos:
            id (string): Identificación única del profesor.
            firstname (string): Nombre del profesor.
            lastname (string): Apellido del profesor.
            username (string): Nombre del profesor en el programa.
            email (string): Correo electrónico del profesor.
            departamento (string): El departamento al que pertenece el profesor.
            seguidores (list): Lista de seguidores.
            tipo (string): Tipo de usuario 'profesor'.
            departamento(string): Departamento donde pertenece.
        """
        self.departamento = departamento
        super().__init__(id, firstname, lastname, username, email, seguidores, tipo)

    def show_teacher(self):
        """
        Muestra la información del profesor en la consola.
        """
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Departamento: {self.departamento}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)
