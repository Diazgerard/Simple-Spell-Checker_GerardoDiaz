# Simple-Spell-Checker_GerardoDiaz

📌 Descripción
Simple Spell Checker es una herramienta básica de corrección ortográfica que sugiere palabras correctas a partir de errores tipográficos. Utiliza la distancia de edición mínima (Levenshtein) para encontrar las sugerencias más cercanas dentro de un pequeño diccionario de palabras.

🎯 Objetivos
Implementar un corrector ortográfico simple.

Usar la distancia de Levenshtein para calcular la similitud entre palabras.

Sugerir las N palabras más cercanas del diccionario para una palabra mal escrita.

⚙️ Funcionamiento
El usuario introduce una palabra que podría contener un error tipográfico.

El corrector compara esta palabra con un diccionario predefinido.

Se calcula la distancia de edición entre la palabra introducida y cada palabra del diccionario.

Se devuelven las N palabras más similares (con menor distancia).

🛠️ Tecnologías usadas
Python 3

Algoritmo de Levenshtein (implementación propia o mediante biblioteca estándar)

Diccionario simple (archivo .txt o lista de palabras)
