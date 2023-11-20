class Post:
    """
    Clase que representa un post.

    Atributos:
        likes (list): Lista de likes del post.
        editor (string): El editor del post.
        tipo (string): El tipo de post.
        caption (list): Lista de comentarios del post.
        fecha (string): La fecha del post.
        etiquetas (list): Lista de etiquetas del post.
        multimedia (Multimedia): Objeto Multimedia asociado al post.

    Metodos:
        __init__(self, editor, tipo, fecha, etiquetas, multimedia):
            Inicializa una instancia de la clase Post.

        show_post(self):
            Muestra la información del post en la consola.
    """
    def __init__(self, editor, tipo, fecha, etiquetas, multimedia):
        """
        Inicializa una instancia de la clase Post.

        Argumentos:
            editor (string): El editor del post.
            tipo (string): El tipo de post.
            fecha (string): La fecha del post.
            etiquetas (list): Lista de etiquetas del post.
            multimedia (Multimedia): Objeto Multimedia asociado al post.
        """
        self.likes = []
        self.editor = editor
        self.tipo = tipo
        self.caption = []
        self.fecha = fecha
        self.etiquetas = etiquetas
        self.multimedia = multimedia
        
    def show_post(self):
        """
        Muestra la información del post en la consola.
        """
        print(f"""
    Likes: {len(self.likes)}   
    Editor: {self.editor}
    Tipo: {self.tipo}
    Fecha: {self.fecha}
    Etiquetas:""")
        for etiqueta in self.etiquetas:
            print(etiqueta)
        
        print("Caption:")
        for caption in self.caption:
            caption.show_comentario()
        
        print("Multimedia:")
        self.multimedia.show_multimedia()


