# Ollama
## Instalar
Windows: https://ollama.com/download/windows

A partir de aqui todo en el terminal de windows; no sé como se llama 
Windows Terminal, Command Prompt, PowerShell

## Modelo
ollama pull llama2

## Probar modelo
ollama run llama2


# Entorno virtual

Muevete a la carpeta que quieras usar

## Crear
```commandline
python -m venv .venv
```

nombre ".venv" es al gusto

## Activar
### En linux
```commandline
source .venv/bin/activate
```

### En windows
```text
.\.venv\Scripts\Activate.ps1
```

## Librería

```commandline
pip install ollama
```

Prueba: 
```commandline
python -c 'import ollama'
```

No tiene que dar ningún error

# Código

```python

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

```

Crear un main.py con el código de arriba

```commandline
python main.py
```

Salida:

```text

--- Generando respuesta desde Ollama local ---

Respuesta:

The sky appears blue because of a phenomenon called Rayleigh scattering, where shorter (blue) wavelengths of light travel further through the atmosphere than longer (red) wavelengths, giving the appearance of a blue sky.
```
