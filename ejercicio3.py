from ollama import chat
import json
from jsonschema import validate

MODELO = "llama3.2:3b"


"""
Ejercicio 3 -> Analizador de sentimientos
Haced que el modelo actúe como un analizador de sentimientos.
Esto quiere decir que a vuestro prompt, tendría que concretar si es positivo, negativo, neutral....
Estableced vosotros los valores posibles.
"""



PROMPT_SISTEMA = "Eres un clasificador de sentimientos."

prompt = """
Clasifica el sentimiento de la siguiente frase.

Frase:
"Este curso de inteligencia artificial es increíble."

Devuelve un JSON con esta estructura:

{
 sentimiento: String
}

Valores posibles:

positivo
negativo
neutral

Devuelve SOLO el JSON.
"""

json_schema = {
    "type": "object",
    "properties": {
        "sentimiento": {
            "type": "string",
            "enum": ["positivo", "negativo", "neutral"]
        }
    },
    "required": ["sentimiento"]
}

VECES_INTENTADO = 1


def comprobarSalida(salida):
    try:
        salidaJson = json.loads(salida)
        print(f"Salida recibida: {salidaJson}")
        validate(instance=salidaJson, schema=json_schema)
    except Exception as e:
        print("Salida incorrecta, reintentando...")
        print(e)
        return False

    return True


def hablarConChat(prompt):
    global VECES_INTENTADO

    response = chat(
        model=MODELO,
        messages=[
            {"role": "system", "content": PROMPT_SISTEMA},
            {"role": "user", "content": prompt},
        ],
    )

    while not comprobarSalida(response["message"]["content"]):
        VECES_INTENTADO += 1
        prompt += f"\nLa salida no es correcta. Intento {VECES_INTENTADO}. Devuelve solo el JSON."

        response = chat(
            model=MODELO,
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": prompt},
            ],
        )


hablarConChat(prompt)