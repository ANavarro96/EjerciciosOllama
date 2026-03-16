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
de la estructura de la salida
"""

MODELO = "llama3.2:3b"
PROMPT_SISTEMA="Responde como si fueses Julio Maldini, un crack del fútbol"


prompt = """
En este ejercicio quiero que me devuelva el top 3 de mejores jugadores
de la historia del Tenerife.

Como lo tengo integrado con una web, la estructura del mensaje tiene que ser un json.
Es un JsonArray, con cada objeto con la misma estructura
{ 
 jugador: String,
 añosJugados: Int,
 dorsal:Int
}

<Ejemplo de salida>
[ { 
 jugador: Pepito,
 añosJugados: 2,
 dorsal:2
}, { 
 jugador: Juanito,
 añosJugados: 5,
 dorsal:4
}]
</Ejemplo de salida>


Devuelve únicamente un String con esta estructura, sin nada más de texto.
No me envuelvas el texto en ´´´json´´´
"""


json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
                "jugador": {"type": "string"},
                "añosJugados": {"type": "integer"},
                "dorsal": {"type": "integer"}
            },
            "required": ["jugador", "añosJugados", "dorsal"]
        }
    }


VECES_INTENTADO = 1

def comprobarSalida(salida):
    try:
        salidaJson = json.loads(salida)
        print(f"salida del fichero {salidaJson}")
        validate(instance=salidaJson, schema=json_schema)
    except Exception as e:
        print("La salida no fue exactamente como se esperaba, volvemos a intentarlo")
        print(e)
        return False

    return True




def hablarConChat(prompt):
     global VECES_INTENTADO
     response = chat(
        model=MODELO,
        messages=[
            {
                'role': 'system',
                'content': PROMPT_SISTEMA,
            },
            {'role': 'user', 'content': prompt},
        ],
    )
     while not comprobarSalida(response["message"]["content"]):
                print(response.message.content)
                VECES_INTENTADO =  VECES_INTENTADO + 1
                prompt += f"\nMe das dado la salida incorractamente, es la {VECES_INTENTADO} que lo haces mal, vuelve a intentarlo"
                response = chat(
                    model=MODELO,
                    messages=[
                        {
                            'role': 'system',
                            'content': PROMPT_SISTEMA,
                        },
                        {'role': 'user', 'content': prompt},
                    ],
                )


hablarConChat(prompt)