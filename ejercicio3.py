from ollama import chat
import json
from jsonschema import validate

MODELO = "llama3.2:3b"


"""
Ejercicio 3 -> Analizador de sentimientos
Haced que el modelo actúe como un analizador de sentimientos.
Esto quiere decir que a vuestro prompt, tendría que concretar si es positivo, negativo, neutral....
Estableced vosotros las categorías posibles.
Probad distintos modelos, ¿cuál es mejor, en vuestra opinión?
"""

PROMPT_SISTEMA = ""
