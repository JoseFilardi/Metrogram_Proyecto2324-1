def validar_email(email):
    """
    Valida la estructura y dominio de un correo electrónico.

    Argumento:
        email (string): Dirección de correo electrónico a validar.

    Returns:
        int: 1 si el correo es válido, -1 si no es válido.
    """
    if email.count('@') == 1:
        if email[0] == "@":
            print("El correo no puede empezar con '@'.")
            return -1
        else:
            partes_email = email.split("@")
            if partes_email[1] == "unimet.edu.ve" or partes_email[1] == "correo.unimet.edu.ve":
                return 1
            else:
                print("Los correos solo pueden ser de los siguientes dominios: 'unimet.edu.ve' o 'correo.unimet.edu.ve' ")
                return -1
    else:
        print("El correo debe contener al menos un '@'.")
        return -1

def validar_values_unique(email, username, id, list_user):
    """
    Valida que los valores de email, username e id sean únicos en una lista de usuarios.

    Args:
        email (string): Dirección de correo electrónico.
        username (string): Nombre de usuario.
        id (string): Identificador único.
        list_user (list): Lista de usuarios.

    Returns:
        bool: True si los valores son únicos, False de lo contrario.
    """
    for user in list_user:
        if user.email == email or user.username == username or user.id == id:
            return False
    
    return True

def validar_email_unique(email, list_user):
    """
    Valida que un correo electrónico sea único en una lista de usuarios.

    Argumento:
        email (strimg): Dirección de correo electrónico.
        list_user (list): Lista de usuarios.

    Returns:
        bool: True si el correo es único, False de lo contrario.
    """
    for user in list_user:
        if user.email == email:
            return False
    
    return True

def validar_username_unique(username, list_user):
    """
    Valida que un string solo contenga letras.

    Argumento:
        string (string): String a validar.

    Returns:
        string: String validado que contiene solo letras.
    """
    for user in list_user:
        if user.username == username:
            return False
    
    return True

def validar_letras(string):
    """
    Valida que un string solo contenga letras.

    Args:
        string (string): String a validar.

    Returns:
        string: String validado que contiene solo letras.
    """
    while not string.isalpha() or len(string) == 0:
        print("Error!!! Dato Inválido.")
        string = input("\nIngrese su nombre: ")

#Validar 
def validar_cedula(cedula):
    pass

def validar_seguidor(user_sesion, username, list_user):
    """
    Valida si un usuario sigue a otro usuario.

    Argumento:
        user_sesion (User): Usuario que está en sesión.
        username (string): Nombre de usuario del usuario a validar.
        list_user (list): Lista de usuarios.

    Returns:
        int: El ID del usuario seguido si es válido, -1 de lo contrario.
    """
    for user in list_user:
        if user.username == username:
            for seguidor in user_sesion.seguidores:
                if seguidor == user.id:
                    return user.id
    
    return -1

