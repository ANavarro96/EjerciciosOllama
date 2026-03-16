from ollama import chat
import json

"""
Ejercicio 6 -> reflexión (difícil)
La reflexión es otro tipo de prompting que consiste en mostrar los errores cometidos al modelo,
y seguir iterando hasta que consigue sacar la salida esperada.
La idea de este ejercicio es pedirle al modelo que genere una función que permita 
validar contraseñas, pero las contraseñas:
- Tienen que tener entre 3 y 6 caracteres
- Contener un '!'
- Contener un dígito
Si no se cumplen alguna de estas condiciones, devolveremos False

Podéis usar la función ejecutarCodigo(codigo), que ejecuta la función que se le pase
como parámetro
"""


MODEL = ""
MAX_ITERACIONES = 3 # modificad el número


def ejecutarCodigo(codigo: str):

    try:
        # el namespace gestiona los nombres de las variables / funciones en python
        namespace = {}
        exec(codigo, namespace)

        # sacamos la función
        validar_contrasena = namespace.get('validar_contrasena') # en tiempo de ejecución
        """
        esto no lo vemos tanto, pero podemos almacenar funciones en variables.
        En lenguajes como C es más común, por el hecho de que son punteros (https://www.it.uc3m.es/pbasanta/asng/course_notes/pointers_to_functions_es.html)
        En Python podemos crear código mientras ejecutamos el código, usando la función exec (https://docs.python.org/3/library/functions.html#exec)
        La verdad es que es una pasada que le podamos pedir código ejecutable a un LLM.
        a la vez que estamos hablando con él.
        Yo estuve probando esto y ni de coña pensaba que iba a funcionar, pero lo hace
        

        """
        if not validar_contrasena:
            return False, "No se encontró la función validar_contrasena"

        # Batería de pruebas
        casos_prueba = [
            ("ab3!", False),  # Menos de 3 caracteres válidos
            ("abc!", False),   # 3 caracteres + ! pero sin dígito
            ("ab3!", True),   # 3 caracteres + ! + dígito - Válido
            ("aB3!", True),   # Válido
            ("abcde!", False),  # 5 caracteres + ! pero sin dígito
            ("abc!1", True),  # Válido
            ("abc!12", False),  # Más de 6 caracteres
            ("ab3!x", True),  # Válido (5 caracteres)
        ]

        errores = []
        for password, esperado in casos_prueba:
            try:
                resultado = validar_contrasena(password)
                if resultado != esperado:
                    errores.append(
                        f"  - validar_contrasena('{password}') devuelve {resultado}, "
                        f" y yo esperaba {esperado}"
                    )
            except Exception as e:
                errores.append(f"Error ejecutando validar_contrasena('{password}'): {str(e)}")

        if errores:
            return False, "Errores encontrados:\n" + "\n".join(errores)
        else:
            return True, "Todo ok!!"

    except Exception as e:
        return False, f"Error ejecutando el código: {str(e)}"


def hablarConChat():

    for iteracion in range(1, MAX_ITERACIONES + 1):
        # todo: suerte


