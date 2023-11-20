class Admin:
    """
    Clase que representa a un administrador.

    Attributes:
        email (string): El correo electrónico del administrador.
        username (string): El nombre de usuario del administrador.
    """

    def __init__(self, email, username):
        """
        Inicializa una nueva instancia de la clase Admin.

        Args:
            email (string): El correo electrónico del administrador.
            username (string): El nombre de usuario del administrador.
        """
        self.email = email
        self.username = username