from ollama import chat
import json
from jsonschema import validate

MODELO = "llama3.2:3b"


"""
Ejercicio 4 -> Extracción de información
Una de los usos que le damos a los LLM es ser capaces de resumir textos e identificar los valores
importantes en un texto.
Por ejemplo, haced que el LLM sea un experto en bases de datos, y que cuando le demos
un enunciado de un ejercicio de bases de datos, sea capaz de identificar los atributos, las entidades
y las relaciones, y que las devuelva en un formato en concreto.
El formato puede ser JSON (ejercicios anteriores), XML, texto plano, en csv...
Similar al ejercicio 2, llevad un conteo de las veces que se ha hecho mal.
"""

