from App import App

def main():
    """
    Función principal que ejecuta la aplicación.

    Realiza las siguientes operaciones:
    1. Inicializa una instancia de la clase App.
    2. Carga datos utilizando los métodos api_perfil y api_post de la instancia de App2.
    3. Llena información sobre carreras y departamentos utilizando los métodos llenado_carreras y llenado_department.
    4. Inicia sesión utilizando el método login de la instancia de App2.

    No recibe argumentos y no devuelve ningún valor.

    """
    app = App()
    
    #Cargar Datos
    app.api_perfil()
    app.api_post()
    app.llenado_carreras()
    app.llenado_department()

    app.login()

main()