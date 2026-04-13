# taller_chatbot_db_tacha
---
Creacion codigo python para chatbot local 
---
Estudiante: Kevin Alejandro Tacha Herrera

Profesor: Diego Alejandro Barragan Vargas

---

Link de este repositorio: https://github.com/KevinTacha/taller_chatbot_db_tacha.git

---

### Chatbot de Sistemas Digitales

**Chatbot educativo** con personalidad de tutor experto en **sistemas digitales**.  
**100% local** – no requiere API Key ni conexión a Internet.  
**Basado en coincidencia de patrones** y palabras clave.  
**Memoria simple** que recuerda el último tema preguntado.  
**Respuestas variadas** gracias a selección aleatoria de frases.

---

### ¿Qué conceptos puede explicar?

- **Compuertas lógicas**: AND, OR, NOT, XOR, NAND, NOR.
- **Flip‑flops y latches**: SR, JK, D, T, latch.
- **Circuitos combinacionales**: sumador (half/full adder), multiplexor, decodificador.
- **Circuitos secuenciales**: contadores, registros de desplazamiento.
- **Arquitectura de computadores**: ALU, CPU, buses, memoria RAM/ROM.
- **Conceptos generales**: sistema digital, sistema binario, tabla de verdad.

---

### Explicacion del codigo:
Atributos
Atributo	Tipo	Descripción
self.nombre	str	Nombre del chatbot ("Chatbot").
self.ultimo_tema	str / None	Guarda la última palabra clave que encontró el bot.
self.respuestas_base	dict	Diccionario con listas de respuestas para saludos, despedidas y casos por defecto.
self.conocimiento	dict	Diccionario que asocia palabras clave (ej: "compuerta and") con su explicación.

# Métodos internos (privados, comienzan con _)
	
_preprocesar(texto)	Convierte a minúsculas, elimina espacios y signos de puntuación (¿?¡!.,;:).
_buscar_respuesta(texto)	Recorre self.conocimiento. Si encuentra una clave dentro del texto, guarda esa clave en self.ultimo_tema y devuelve la respuesta asociada.
_responder_saludo(texto)	Busca patrones como "hola", "buenas", "hey". Si los encuentra, devuelve un saludo aleatorio.
_responder_despedida(texto)	Detecta palabras como "adios", "salir", "nos vemos" y devuelve una despedida aleatoria.
_responder_agradecimiento(texto)	Reconoce "gracias", "thanks", "agradecido" y responde con un mensaje fijo.
_preguntar_aclaracion()	Con un 30% de probabilidad (si existe self.ultimo_tema) sugiere profundizar en ese tema.
obtener_respuesta(mensaje_usuario)	Método público principal. Orquesta el flujo:
1. Despedida → 2. Saludo → 3. Agradecimiento → 4. Búsqueda en conocimiento → 5. Respuesta por defecto.

# Funcion Main

Crea una instancia de ChatbotDigital.

Muestra un mensaje de bienvenida.

Entra en un bucle infinito while True.

Lee la entrada del usuario con input().

Si el usuario escribe salir, adios, chao, exit o quit, termina el programa mostrando una despedida.

En caso contrario, llama a bot.obtener_respuesta(usuario) e imprime la respuesta.

# Puntos claves del codigo 

Uso de re.sub() para normalizar el texto

def _preprocesar(self, texto):
    texto = texto.lower().strip()
    texto = re.sub(r'[¿?¡!.,;:]', '', texto)
    return texto

Búsqueda lineal en el diccionario de conocimiento

def _buscar_respuesta(self, texto):
    for clave, respuesta in self.conocimiento.items():
        if clave in texto:
            self.ultimo_tema = clave
            return respuesta
    return None
    
# Por qué es clave:

Es una coincidencia de subcadenas simple, no requiere IA compleja.

Almacena self.ultimo_tema para que el bot pueda ofrecer profundización después.

El orden de las claves importa: si dos claves coinciden, se usará la primera que aparezca (ej: "flip flop" antes que "flip flop jk"). Por eso en el diccionario se colocan primero las más genéricas.

# Respuestas aleatorias para evitar monotonía

self.respuestas_base = {
    "saludo": [
        "¡Hola! Soy Chatbot...",
        "¡Bienvenido! Pregúntame sobre...",
        "Hola, ¿qué concepto...?"
    ],
    ...
}

# Profundización probabilística (memoria simple)

def _preguntar_aclaracion(self):
    if self.ultimo_tema and random.random() < 0.3:
        return f"¿Te gustaría profundizar en {self.ultimo_tema} o prefieres otro tema?"
    return None

No siempre ofrece profundizar (30% de probabilidad), evitando ser repetitivo.

Utiliza self.ultimo_tema que se actualiza cada vez que se encuentra una coincidencia.

Es una forma muy ligera de memoria contextual sin necesidad de guardar historiales largos.

# Orden de prioridad en obtener_respuesta()

resp = self._responder_despedida(mensaje_proc)
if resp: return resp
resp = self._responder_saludo(mensaje_proc)
if resp: return resp
resp = self._responder_agradecimiento(mensaje_proc)
if resp: return resp
resp = self._buscar_respuesta(mensaje_proc)
if resp:
    sugerencia = self._preguntar_aclaracion()
    if sugerencia:
        resp += " " + sugerencia
    return resp
return random.choice(self.respuestas_base["default"])

Las despedidas tienen la máxima prioridad (si el usuario dice "adios" no debe responder otra cosa).

Los saludos y agradecimientos van antes que la búsqueda de conocimiento para que el bot sea cordial.

Sólo si nada de eso coincide, se intenta responder una pregunta técnica.

Al final, un mensaje por defecto evita que el bot se quede callado.

# Manejo de KeyboardInterrupt y palabras de salida

try:
    usuario = input("Tú: ")
    if usuario.lower() in ["salir", "adios", "chao", "exit", "quit"]:
        print(f"🤖 {bot.nombre}: {bot.obtener_respuesta(usuario)}")
        break
    ...
except KeyboardInterrupt:
    print("\n Chatbot: ¡Hasta luego!")
    break

El bucle principal captura Ctrl+C para salir sin mostrar un traceback feo.

Se contemplan múltiples formas de salir (salir, adios, chao, exit, quit) tanto en minúsculas como en mayúsculas gracias a .lower().

La despedida también se muestra cuando el usuario escribe una palabra de salida, gracias a que obtener_respuesta() reconoce esas palabras.

# Estructura de datos para el conocimiento

El diccionario self.conocimiento mezcla conceptos muy específicos ("flip flop jk") con otros más generales ("flip flop").
Ventaja: Permite responder tanto a preguntas amplias como detalladas.
Precaución: Si se invierte el orden (primero "flip flop" y luego "flip flop jk"), la pregunta "flip flop jk" coincidiría con "flip flop" y nunca se usaría la respuesta más específica. Por eso en el código actual las claves están ordenadas de más específicas a más genéricas (aunque no es visible en el README, en el archivo original se colocaron agrupadas por tema, pero el orden de inserción en Python 3.7+ mantiene el orden, así que hay que tener cuidado).

---

### Resultado Esperado:

<p align="center">
<img src="imagenes/chatbot1.jpeg" width="500">
<p/>


