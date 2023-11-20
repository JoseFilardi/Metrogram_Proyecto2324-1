class Comentario:
    """
    Clase que representa un comentario.

    Atributos:
        user (string): El nombre del usuario que hizo el comentario.
        caption (string): El contenido del comentario.

    Metodos:
        __init__(self, user, caption):
            Inicializa una instancia de la clase Comentario.

        show_comentario(self):
            Muestra la representación del comentario en la consola.
    """
    def __init__(self, user, caption):
        """
        Inicializa una instancia de la clase Comentario.

        Argumentos:
            user (string): El nombre del usuario que hizo el comentario.
            caption (string): El contenido del comentario.
        """
        self.user = user
        self.caption = caption
    
    def show_comentario(self):
        """
        Muestra la representación del comentario en la consola.
        """
        print(f"{self.user}: {self.caption}")


