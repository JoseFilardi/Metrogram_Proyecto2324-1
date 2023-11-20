class Multimedia:
    """
    Clase que representa un objeto multimedia.

    Atributos:
        tipo (string): Tipo de multimedia (por ejemplo, 'imagen', 'video', etc.).
        url (string): URL que apunta al recurso multimedia.

    Metodos:
        __init__(self, tipo, url):
            Inicializa la instancia de la clase Multimedia.

        show_multimedia(self):
            Muestringa la información de la multimedia en la consola.
    """
    def __init__(self, tipo, url):
        """
        Inicializa la instancia de la clase Multimedia.

        Argumentos:
            tipo (string): Tipo de multimedia (por ejemplo, 'imagen', 'video', etc.).
            url (string): URL que apunta al recurso multimedia.
        """
        self.tipo = tipo
        self.url = url

    def show_multimedia(self):
        """
        Muestra la información de la multimedia en la consola.
        """
        print(f"""
        Tipo: {self.tipo}, Url: {self.url}
    """)
