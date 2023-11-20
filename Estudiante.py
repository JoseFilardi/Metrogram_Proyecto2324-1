from User import User

class Estudiante(User):
    """
    Clase que representa a un estudiante, heredada de la clase User.

    Atributos:
        carrera (string): La carrera del estudiante.
        id (int): Identificación única del estudiante.
        firstname (string): Nombre del estudiante.
        lastname (string): Apellido del estudiante.
        username (string): Nombre de usuario del estudiante.
        email (string): Correo electrónico del estudiante.
        seguidores (list): Lista de seguidores.
        tipo (string): Tipo de usuario 'estudiante'.

    Métodos:
        __init__(self, id, firstname, lastname, username, email, carrera, seguidores, tipo):
            Inicializa la instancia de la clase Estudiante.

        show_student(self):
            Muestra la información del estudiante en la consola.
    """
    def __init__(self, id, firstname, lastname, username, email, carrera, seguidores, tipo):
        """
        Inicializa la instancia de la clase Estudiante.

        Argumentos:
            id (int): Identificación única del estudiante.
            firstname (string): Nombre del estudiante.
            lastname (string): Apellido del estudiante.
            username (string): Nombre de usuario del estudiante.
            email (string): Correo electrónico del estudiante.
            carrera (string): La carrera del estudiante.
            seguidores (list): Lista de seguidores.
            tipo (string): Tipo de usuario 'estudiante'.
        """
        self.carrera = carrera
        super().__init__(id, firstname, lastname, username, email, seguidores, tipo)

    def show_student(self):
        """
        Muestra la información del estudiante en la consola.
        """
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Carrera: {self.carrera}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)
