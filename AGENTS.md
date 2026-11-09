# primeros_pasos_con_ollama

Guía de primeros pasos con Ollama y Python: instalación del modelo, entorno virtual y una llamada de prueba con la librería `ollama`.

## Visibilidad y rama

- Público.
- Rama por defecto: `main`.

## Stack

- Python 3 con la librería `ollama`. No hay `requirements.txt`.
- Ollama como servidor local.

## Estructura

- `README.md`: guía completa (instalar Ollama, modelo `llama2`, entorno virtual, `pip install ollama`, código de prueba).
- `main.py`: script de prueba que llama a `ollama.chat(model='llama2', ...)` y muestra la respuesta.

## Comandos

Del README (no ejecutados):

- Modelo: `ollama pull llama2` y `ollama run llama2`.
- Entorno: `python -m venv .venv && source .venv/bin/activate` (Linux) y `pip install ollama`.
- Comprobar librería: `python -c 'import ollama'`.
- Ejecutar: `python main.py`.
- Tests: no hay.

## Configuración

- Sin variables de entorno ni ficheros de config.
- Servidor Ollama en el host por defecto de la librería (no hay URL codificada).
- Modelo `llama2` codificado en `main.py`.

## Convenciones para agentes

- El README está pensado para Windows y Linux: mantener ambas secciones de activación del venv.
- Mantener el texto en español y el código con comentarios en español.
- No añadir dependencias fuera de `ollama` sin necesidad.

## Estado

- Repo de aprendizaje, pequeño y sin tests.
- Atención: el README dice "Windows" para la instalación de Ollama, pero el código no depende del sistema operativo.
- Atención: `main.py` no comprueba que el modelo `llama2` esté descargado; si falta, la llamada falla y el manejo de error solo imprime el mensaje genérico.
- Atención: el README tiene un bloque de código con la función y el `if __name__` duplicados respecto a `main.py` (no verificado).
