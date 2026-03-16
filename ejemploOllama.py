from ollama import chat


# chat(model, messages, stream=False, options=None):
# - model: nombre del modelo en Ollama (por ejemplo, 'llama3.2').
# - messages: lista de mensajes, un diccionario con  las claves:
#       - 'role': 'system'|'user'|'assistant'
#       - 'content': 'el prompt asociado'.
# - stream: opcional, True para respuesta en streaming, es decir, que vamos sacando
#   la info a medida que el modelo la v a generando. Si no, recibimos todo lo que
#    escupa el modelo a la vez.
# - options: opcional, ajustes de generación (temperature, num_predict, etc.).
response = chat(
    model='llama3.2:3b',
    messages=[
        {
            'role': 'system',
            'content': (
                'Responde como si fueses el famoso streamer espanol, elXokas. '
                'ElXokas es conocido por su estilo agresivo, insultando bastante.'
            ),
        },
        {'role': 'user', 'content': 'Que campeon del Lol es mejor?'},
    ],
    options={
        'temperature': 0.7,
        'num_predict': 120,
        'top_p': 0.9,
    },
)

print(type(response))
# por si queréis verlo -> print(response)
# response es un objeto de clase ChatResponse (https://docs.spring.io/spring-ai/docs/current/api/org/springframework/ai/ollama/api/OllamaApi.ChatResponse.html)
for clave,valor  in list(response):
    try:
        print(f"{clave} --> {response[clave] }")
    except KeyError:
        continue # ignoro los errores :)

# De aquí la más importante es["message"]["content"]
print(f"ElXokas dice > {response["message"]["content"]}")
