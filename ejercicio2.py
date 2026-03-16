from ollama import chat
import json
from jsonschema import validate
from pydantic import BaseModel

MODELO = "llama3.2:3b"

"""
Ejercicio 2 -> Extracción de información
Haced que el modelo reciba una frase con una estructura concreta, y la traduzca a json únicamente.
Por ejemplo, que reciba frases del estilo "Mi gato se llama rayitas, pesa 4 kilos y es naranja"
Y devuelva un json del estilo 
{
"gatito":"rayitas",
"kilos":4,
"color":"Naranja"
}

Hacedlo en dos partes:
1 - Conseguid primero que os devuelve un string con la estructura que queréis.
2 - Usad Pydantic, o json_schema para validar la salida. Si la salida no es correcta,
volved a pedidle al LLM que genere el json, así hasta que acierte.
"""



PROMPT_SISTEMA = ""

prompt = """
"""


"""¿Recordáis Pydantic (https://docs.pydantic.dev/latest/)?"""
def recordarPydantic():
    class Botella(BaseModel):
     liquido: str
     cantidad: int

    botella = '{ "liquido":"agua", "cantidad":500}'

    print(Botella.model_validate_json(botella)) # ok
    try:
        print(Botella.model_validate_json("{}")) # excepcion
    except Exception as e:
        print(f" Error al validar el json {e}")

recordarPydantic()



# Posible estructura del ejercicio.
# # Contador que hay que aumentar en 1 si el LLM no consigue parsear la salida a un JSON correctamente.
# VECES_INTENTADO = 1
#
#
# def comprobarSalida(salida):
#     try:
#       # todo
#     except Exception as e:
#         print("Salida incorrecta, reintentando...")
#         print(e)
#         return False
#     return True
#
#
# def hablarConChat(prompt):
#     global VECES_INTENTADO
#
#     response = # todo: obtener respuesta del chat
#
#     while not comprobarSalida(response["message"]["content"]):
#         VECES_INTENTADO += 1
#        # todo: modificar prompt
#
#
#         response = # todo
#
#
# hablarConChat(prompt)