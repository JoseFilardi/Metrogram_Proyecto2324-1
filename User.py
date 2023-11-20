class User:
    """
    Clase que representa a los usuario.

    Atributos:
        id (strig): Identificación única del usuario.
        firstname (strig): Nombre del usuario.
        lastname (strig): Apellido del usuario.
        username (strig): Nombre en el programa.
        email (strig): Correo electrónico del usuario.
        seguidores (list): Lista de seguidores.
        tipo (strig): Tipo de usuario (puede ser 'estudiante' u 'profesor').

    Metodos:
        __init__(self, id, firstname, lastname, username, email, seguidores, tipo):
            Inicializa la instancia de la clase User.

        show_user(self):
            Muestra la información del usuario en la consola.
    """
    def __init__(self, id, firstname, lastname, username, email, seguidores, tipo):
        """
        Inicializa la instancia de la clase User.

        Argumentos:
            id (string): Identificación única del usuario.
            firstname (strig): Nombre del usuario.
            lastname (strig): Apellido del usuario.
            username (strig): Nombre en el programa.
            email (strig): Correo electrónico del usuario.
            seguidores (list): Lista de seguidores.
            tipo (strig): Tipo de usuario (puede ser 'estudiante' u 'profesor').
        """
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.seguidores = seguidores
        self.tipo = tipo

    def show_user(self):
        """
        Muestra la información del usuario en la consola.
        """
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)
