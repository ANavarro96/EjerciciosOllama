from json import JSONDecodeError

import jsonschema
from ollama import chat
import json
from jsonschema import validate
from pydantic import ValidationError

"""
Ejercicio 5 -> k-shot prompting
Vamos a obligar al modelo a que responda con el patrón que esperamos.
Si queremos conectar nuestro modelo con algún software ya existente, esta conexión tendrá que seguir
una estructura esperada (json/xml), y no podemos arriesgarnos a que el LLM devuelva algo en una estructura incorrecta y el sistema de error
o se caiga.
El k-shot promprting es muy útil para asegurarnos que la respuesta es la correcta, asociando al prompt unos cuantos ejemplos
de la estructura de la salida.
Ya hemos visto la importancia de usar prompts concretos y explicativos, pero en este caso
escribe un prompt (mejores juegos de consola de la historia), pero añadiendo a él,
3 o 4 ejemplos de la estructura esperada.
¿Es más eficaz esto que la reflexión?
"""

MODELO = ""
PROMPT_SISTEMA=""

