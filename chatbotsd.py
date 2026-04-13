import re
import random

class ChatbotDigital:
    def __init__(self):
        self.nombre = "Chatbot"
        self.ultimo_tema = None
        self.respuestas_base = {
            "saludo": [
                "¡Hola! Soy Chatbot, tu experto en sistemas digitales. ¿En qué puedo ayudarte?",
                "¡Bienvenido! Pregúntame sobre compuertas lógicas, circuitos, arquitectura de computadores...",
                "Hola, ¿qué concepto de sistemas digitales te gustaría repasar hoy?"
            ],
            "despedida": [
                "¡Hasta luego! Sigue practicando con circuitos digitales.",
                "Nos vemos. Recuerda: ¡la lógica binaria es la base de todo!",
                "Adiós. Si tienes más dudas, vuelve cuando quieras."
            ],
            "default": [
                "No estoy seguro de entender tu pregunta. ¿Podrías preguntar sobre compuertas lógicas, flip-flops, sumadores o arquitectura de computadores?",
                "Ese tema no lo domino todavía. Intenta preguntarme sobre sistemas digitales (AND, OR, flip-flops, etc.).",
                "Como tutor de sistemas digitales, enfócate en temas como lógica combinacional, secuencial o arquitectura de CPUs."
            ]
        }
        
        # Base de conocimientos (palabra clave -> respuesta)
        self.conocimiento = {
            # Compuertas lógicas
            "compuerta and": "La compuerta AND tiene salida 1 solo si TODAS sus entradas son 1. Ejemplo: 1 AND 1 = 1; 1 AND 0 = 0.",
            "compuerta or": "La compuerta OR da salida 1 si al menos una entrada es 1. Ejemplo: 1 OR 0 = 1; 0 OR 0 = 0.",
            "compuerta not": "El NOT (inversor) invierte la entrada: 0 -> 1, 1 -> 0.",
            "compuerta xor": "XOR da 1 cuando las entradas son diferentes. Es la base de los sumadores.",
            "compuerta nand": "NAND es AND negado. Salida 0 solo si todas las entradas son 1.",
            "compuerta nor": "NOR es OR negado. Salida 1 solo si todas las entradas son 0.",
            
            # Flip-flops
            "flip flop": "Un flip-flop es un biestable que almacena 1 bit. Puede ser SR, JK, D o T.",
            "flip flop sr": "El SR tiene entradas Set (pone 1) y Reset (pone 0). Estado prohibido: S=1,R=1.",
            "flip flop jk": "JK soluciona el estado prohibido del SR. Con J=1,K=1 alterna su salida.",
            "flip flop d": "El flip-flop D copia la entrada D a la salida Q en cada pulso de reloj.",
            "flip flop t": "El T flip-flop alterna su salida (toggle) cuando T=1 y llega el reloj.",
            "latch": "Un latch es un flip-flop sin reloj; cambia cuando cambian las entradas.",
            
            # Circuitos combinacionales
            "sumador": "Un sumador binario suma dos bits (half-adder) o dos bits más acarreo (full-adder).",
            "half adder": "Half adder: suma dos bits → suma (XOR) y acarreo (AND).",
            "full adder": "Full adder suma dos bits + acarreo de entrada. Se construye con dos half adders.",
            "multiplexor": "Un multiplexor (MUX) selecciona una de varias entradas mediante señales de control.",
            "decodificador": "Decodificador convierte un código binario en una sola línea activa (1 de N).",
            
            # Circuitos secuenciales
            "contador": "Contador digital: secuencia de estados sincronizada por reloj (ej. 0,1,2,3...).",
            "registro": "Registro de desplazamiento almacena y mueve bits en cada pulso de reloj.",
            
            # Arquitectura de computadores
            "alu": "ALU (Unidad Aritmético-Lógica) realiza operaciones aritméticas y lógicas en la CPU.",
            "bus": "Un bus es un conjunto de líneas que transmiten datos, direcciones o control.",
            "memoria ram": "RAM: memoria de acceso aleatorio, volátil, donde se ejecutan programas.",
            "memoria rom": "ROM: memoria de solo lectura, no volátil, para firmware o booteo.",
            "cpu": "La CPU (Unidad Central de Procesamiento) ejecuta instrucciones: fetch, decode, execute.",
            
            # Preguntas generales
            "sistema digital": "Un sistema digital procesa información en forma de dígitos binarios (0/1).",
            "binario": "El sistema binario usa solo dos dígitos: 0 y 1. Es la base de la electrónica digital.",
            "tabla de verdad": "Una tabla de verdad enumera todas las combinaciones de entrada y su salida correspondiente.",
        }
    
    def _preprocesar(self, texto):
        """Limpia y normaliza el texto del usuario."""
        texto = texto.lower().strip()
        # Eliminar signos de puntuación comunes
        texto = re.sub(r'[¿?¡!.,;:]', '', texto)
        return texto
    
    def _buscar_respuesta(self, texto):
        """Busca coincidencia de palabra clave en el conocimiento."""
        for clave, respuesta in self.conocimiento.items():
            if clave in texto:
                self.ultimo_tema = clave
                return respuesta
        return None
    
    def _responder_saludo(self, texto):
        patrones_saludo = ["hola", "buenas", "saludos", "hey", "que tal"]
        if any(p in texto for p in patrones_saludo):
            return random.choice(self.respuestas_base["saludo"])
        return None
    
    def _responder_despedida(self, texto):
        patrones_despedida = ["adios", "chao", "hasta luego", "salir", "nos vemos", "terminar"]
        if any(p in texto for p in patrones_despedida):
            return random.choice(self.respuestas_base["despedida"])
        return None
    
    def _responder_agradecimiento(self, texto):
        if any(p in texto for p in ["gracias", "thanks", "agradecido"]):
            return "¡De nada! Me alegra ayudarte con sistemas digitales. ¿Algo más?"
        return None
    
    def _preguntar_aclaracion(self):
        """Si el usuario menciona un tema anterior, ofrece más info."""
        if self.ultimo_tema and random.random() < 0.3:  # 30% de probabilidad
            return f"¿Te gustaría profundizar en {self.ultimo_tema} o prefieres otro tema?"
        return None
    
    def obtener_respuesta(self, mensaje_usuario):
        """Método principal para obtener respuesta del chatbot."""
        mensaje_proc = self._preprocesar(mensaje_usuario)
        
        # 1. Despedida
        resp = self._responder_despedida(mensaje_proc)
        if resp:
            return resp
        
        # 2. Saludo
        resp = self._responder_saludo(mensaje_proc)
        if resp:
            return resp
        
        # 3. Agradecimiento
        resp = self._responder_agradecimiento(mensaje_proc)
        if resp:
            return resp
        
        # 4. Buscar en conocimiento
        resp = self._buscar_respuesta(mensaje_proc)
        if resp:
            # Añadir posible sugerencia de profundización
            sugerencia = self._preguntar_aclaracion()
            if sugerencia:
                resp += " " + sugerencia
            return resp
        
        # 5. Respuesta por defecto
        return random.choice(self.respuestas_base["default"])

# ============================================
# PROGRAMA PRINCIPAL
# ============================================
def main():
    bot = ChatbotDigital()
    print("Chatbot - Tu asistente de Sistemas Digitales (sin Internet)")
    print("Escribe 'salir' o 'adios' para terminar.\n")
    
    while True:
        try:
            usuario = input("Tú: ")
            if usuario.lower() in ["salir", "adios", "chao", "exit", "quit"]:
                print(f" {bot.nombre}: {bot.obtener_respuesta(usuario)}")
                break
            respuesta = bot.obtener_respuesta(usuario)
            print(f" {bot.nombre}: {respuesta}")
        except KeyboardInterrupt:
            print("\n Chatbot: ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
