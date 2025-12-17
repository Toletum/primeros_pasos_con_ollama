import ollama


def test_local_model():
    print("--- Generando respuesta desde Ollama local ---")

    try:
        response = ollama.chat(model='llama2', messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue? Answer in one short sentence in English.',
            },
        ])

        # Imprimir la respuesta del modelo
        print("\nRespuesta:")
        print(response['message']['content'])

    except Exception as e:
        print(f"Error al conectar con Ollama: {e}")
        print("Asegúrate de que la aplicación Ollama esté ejecutándose.")


if __name__ == "__main__":
    test_local_model()
