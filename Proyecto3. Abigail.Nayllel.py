import random
import datetime
import tkinter as tk

ventana = tk.Tk()

ventana.title("Mundial FIFA 2026 uwu")
ventana.geometry("1000x600")
ventana.configure(bg="#0f172a")

titulo = tk.Label(
    ventana,
    text="MUNDIAL FIFA 2026",
    font=("Arial", 24, "bold"),
    fg="pink"

)

titulo.pack(pady=30)

def openPaises():
    ventanita = tk.Toplevel()
    ventanita.title("Países y Selecciones uwu")
    ventanita.geometry("700x500")

def mostrar_Jugadores():
    ventanita = tk.Toplevel()
    ventanita.title("Entrenadores y Jugadores")
    ventanita.geometry("700x500")

def abrirMundial():
    ventanita = tk.Toplevel()
    ventanita.title("Configurar Mundial")
    ventanita.geometry("700x500")

def jugarMundial():
    ventanita = tk.Toplevel()
    ventanita.title("Jugar Mundial")
    ventanita.geometry("700x500")

def verEstadisticas():
    ventanita = tk.Toplevel()
    ventanita.title("Estadísticas")
    ventanita.geometry("700x500")

btw_paises= tk.Button(
    ventana,
    text= "Administrar Países y Selecciones",
    width=35,
    height=2,
    command= openPaises
)

btw_paises.pack(pady=10)

btw_entrenadores= tk.Button(
    ventana,
    text= "Entrenadores y Jugadores",
    width=35,
    height=2,
    command= mostrar_Jugadores
)

btw_entrenadores.pack(pady=10)

btw_entrenadores= tk.Button(
    ventana,
    text= "Configurar Mundial",
    width=35,
    height=2,
    command= abrirMundial
)

btw_entrenadores.pack(pady=10)

btw_entrenadores= tk.Button(
    ventana,
    text= "Jugar Mundial",
    width=35,
    height=2,
    command= jugarMundial
)

btn_jugar.pack(pady=10)

btw_entrenadores= tk.Button(
    ventana,
    text= "Estadísticas y Rankings",
    width=35,
    height=2,
    command= verEstadisticas
)

btw_estadisticasuwu.pack(pady=10)

ventana.mainloop()

"""
Nombre de clase: Persona
Entradas: nombre, apellido, fecha_nacimiento, nacionalidad
Salidas: ninguna
Restricciones:
               nombre, apellido, fecha_nacimiento y nacionalidad deben ser cadenas de texto no vacías
Función: representa una persona con atributos básicos como nombre, apellido, fecha de nacimiento y nacionalidad, y una función para mostrar sus datos.
"""
class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("Error: nombre inválido o vacio")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("Error: apellido inválido o vacio")
        if not isinstance(fecha_nacimiento, str) or fecha_nacimiento.strip() == "":
            raise ValueError("Error: fecha de nacimiento inválida o vacia")
        if not isinstance(nacionalidad, str) or nacionalidad.strip() == "":
            raise ValueError("Error: nacionalidad inválida o vacia")
        
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad


    """
    Nombre: mostrar_datos
    Entradas: ninguna
    Salidas: imprime los datos de la persona
    Restricciones: ninguna
    Función: muestra los datos de la persona en un formato legible"""
    def mostrar_datos(self):
        print(f"""Nombre: {self.nombre + " " + self.apellido}
        Fecha nacimiento: {self.fecha_nacimiento}
        Nacionalidad: {self.nacionalidad}""")


"""
Nombre de clase: Entrenador
Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_años, sistema_juego
Salidas: ninguna
Restricciones:
               nombre, apellido, fecha_nacimiento y nacionalidad deben ser  texto y no estar vacios
               licencia, experiencia_años y sistema_juego deben cumplir con sus respectivas validaciones
Función: representa un entrenador de fútbol, heredando de la clase Persona, con atributos adicionales como licencia, años de experiencia y sistema de juego, y funciones para mostrar y actualizar sus datos.
"""
class Entrenador(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_años, sistema_juego):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)
        
        if not isinstance(licencia, str) or licencia.strip() == "":
            raise ValueError("Error: licencia inválida")
        if not isinstance(experiencia_años, int) or experiencia_años < 0:
            raise ValueError("Error: la experiencia debe ser un número entero positivo")
        if not isinstance(sistema_juego, str) or sistema_juego.strip() == "":
            raise ValueError("Error: sistema de juego inválido")
        
        self.licencia = licencia
        self.experiencia_años = experiencia_años
        self.sistema_juego = sistema_juego
    """
    Nombre: mostrar_datos
    Entradas: ninguna
    Salidas: imprime los datos del entrenador, incluyendo los datos heredados de Persona
    Restricciones: ninguna
    Función: muestra los datos del entrenador, incluyendo los datos heredados de Persona, en un formato legible
    """
    def mostrar_datos(self):
        Persona.mostrar_datos(self)
        print(f"""Licencia: {self.licencia}
        Experiencia: {self.experiencia_años} años
        Sistema de juego: {self.sistema_juego}""")
    
    """
    Nombre: actualizar_datos
    Entradas: licencia (opcional), experiencia_años (opcional), sistema_juego (opcional)
    Salidas: ninguna
    Restricciones: las entradas deben cumplir con sus respectivas validaciones
    Función: actualiza los datos del entrenador, incluyendo los datos heredados de Persona
    """
    def actualizar_datos(self, licencia=None, experiencia_años=None, sistema_juego=None):
        #Se utiliza none para permitir actualizar solo algunos de los atributos sin necesidad de proporcionar todos los datos nuevamente
        if not licencia == None:
            if not isinstance(licencia, str) or licencia.strip() == "": #Se utiliza el método strip() para eliminar espacios por si el usuario ingresa unicamente espacios en el str
                raise ValueError("Error: licencia inválida")
            self.licencia = licencia
        
        if not experiencia_años == None:
            if not isinstance(experiencia_años, int) or experiencia_años < 0:
                raise ValueError("Error: experiencia inválida")
            self.experiencia_años = experiencia_años
        
        if not sistema_juego == None:
            if not isinstance(sistema_juego, str) or sistema_juego.strip() == "":
                raise ValueError("Error: sistema de juego inválido")
            self.sistema_juego = sistema_juego
"""
Nombre de clase: Futbolista
Entradas: nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual
Salidas: ninguna
Restricciones:
               nombre, apellido, fecha_nacimiento y nacionalidad deben ser texto y no estar vacios
               dorsal debe ser un número entero entre 1 y 99
               posicion debe ser una de las siguientes opciones: "Portero", "Defensa", "Mediocampista", "Delantero"
               puntaje_individual debe ser un número entero entre 1 y 100
Función: representa un futbolista, heredando de la clase Persona, con atributos adicionales como dorsal, posición y puntaje individual, y funciones para mostrar y actualizar sus datos, registrar goles, asistencias y tarjetas.
"""
class Futbolista(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)
        
        if not isinstance(dorsal, int) or dorsal < 1 or dorsal > 99:
            raise ValueError("Error: el dorsal debe ser un número entre 1 y 99")
        
        posiciones_validas = ["Portero", "Defensa", "Mediocampista", "Delantero"]
        for pos in posiciones_validas:  #Este for sirve para validar la posición ingresada por el usuario, tomando como referencia la lista anteriormente brindada 
            if pos.lower() == posicion.lower():  #Se utilizo el lower() para permitir que el usuario ingrese la posición sin importar mayúsculas o minúsculas
                posicion = pos
                break
        else:
            raise ValueError(f"Error: posición inválida. Debe ser una de: {posiciones_validas}")
        
        if not isinstance(puntaje_individual, int) or puntaje_individual < 1 or puntaje_individual > 100:
            raise ValueError("Error: el puntaje individual debe estar entre 1 y 100")
        
        self.dorsal = dorsal
        self.posicion = posicion
        self.puntaje_individual = puntaje_individual
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.goles = 0
        self.asistencias = 0
    """
    Nombre: mostrar_datos
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: muestra los datos del futbolista, incluyendo los datos heredados de Persona, en un formato legible
    """
    def mostrar_datos(self):
        Persona.mostrar_datos(self)
        print(f"""Dorsal: {self.dorsal}
        Posición: {self.posicion}
        Puntaje individual: {self.puntaje_individual}
        Goles: {self.goles}
        Asistencias: {self.asistencias}
        Tarjetas amarillas: {self.total_tarjetas_amarillas}
        Tarjetas rojas: {self.total_tarjetas_rojas}""")
    
    """
    Nombre: actualizar_datos
    Entradas: dorsal (opcional), posicion (opcional), puntaje_individual (opcional)
    Salidas: ninguna
    Restricciones: las entradas deben cumplir con sus respectivas validaciones
    Función: actualiza los datos del futbolista, incluyendo los datos heredados de Persona
    """
    def actualizar_datos(self, dorsal=None, posicion=None, puntaje_individual=None):
        #Se utiliza none para permitir actualizar solo algunos de los atributos sin necesidad de brindar todos los datos nuevamente
        if not dorsal == None:
            if not isinstance(dorsal, int) or dorsal < 1 or dorsal > 99:
                raise ValueError("Error: el dorsal debe ser un número entre 1 y 99")
            self.dorsal = dorsal
        
        if not posicion == None:
            posiciones_validas = ["Portero", "Defensa", "Mediocampista", "Delantero"]
            for pos in posiciones_validas:
                if pos.lower() == posicion.lower():
                    posicion = pos
                    break
            else:
                raise ValueError(f"Error: posición inválida. Debe ser una de: {posiciones_validas}")
            self.posicion = posicion
        
        if not puntaje_individual == None:
            if not isinstance(puntaje_individual, int) or puntaje_individual < 1 or puntaje_individual > 100:
                raise ValueError("Error: el puntaje individual debe estar entre 1 y 100")
            self.puntaje_individual = puntaje_individual
    
    """
    Nombre: registrar_gol
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: registra un gol marcado por el futbolista
    """
    def registrar_gol(self):
        self.goles += 1 


    """
    Nombre: registrar_asistencia
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: registra una asistencia realizada por el futbolista
    """
    def registrar_asistencia(self):
        self.asistencias += 1

    """
    Nombre: registrar_tarjeta
    Entradas: tipo (string)
    Salidas: ninguna
    Restricciones: tipo debe ser "amarilla" o "roja"
    Función: registra una tarjeta amarilla o roja recibida por el futbolista, incrementando el contador correspondiente
    """
    def registrar_tarjeta(self, tipo):
        if tipo.lower() == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo.lower() == "roja":
            self.total_tarjetas_rojas += 1
        else:
            raise ValueError("Error: tipo de tarjeta inválido. Debe ser 'amarilla' o 'roja'")
"""
Nombre de clase: Pais
Entradas: codigo_fifa, nombre, continente, ranking_fifa
Salidas: ninguna
Restricciones:
               codigo_fifa debe ser una cadena de texto de exactamente 3 caracteres
               nombre y continente deben ser cadenas de texto no vacías
               ranking_fifa debe ser un número entero entre 1 y 100 
Función: representa un país con atributos como código FIFA, nombre, continente y ranking FIFA, y funciones para mostrar y actualizar sus datos.
"""
class Pais():
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):
        if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3:
            raise ValueError("Error: código FIFA inválido o vacio, debe contener exactamente 3 caracteres")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("Error: nombre del país inválido o vacio")
        if not isinstance(continente, str) or continente.strip() == "":
            raise ValueError("Error: continente inválido o vacio")
        if not isinstance(ranking_fifa, int) or ranking_fifa < 1 or ranking_fifa > 100:
            raise ValueError("Error: ranking FIFA debe ser un número entero positivo entre 1 y 100")
        
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.continente = continente
        self.ranking_fifa = ranking_fifa
    

    """
    Nombre: mostrar_datos
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: muestra los datos del país
    """
    def mostrar_datos(self):
        print(f"""Código FIFA: {self.codigo_fifa}
        Nombre: {self.nombre}
        Continente: {self.continente}
        Ranking FIFA: {self.ranking_fifa}""")

    
    """
    Nombre: actualizar_datos
    Entradas: codigo_fifa (opcional), nombre (opcional), continente (opcional), ranking_fifa (opcional)
    Salidas: ninguna
    Restricciones: las entradas deben cumplir con sus respectivas validaciones
    Función: actualiza los datos del país
    """
    def actualizar_datos(self, codigo_fifa=None, nombre=None, continente=None, ranking_fifa=None):  
        #Se utiliza none para permitir actualizar solo algunos de los atributos sin necesidad de brindar todos los datos nuevamente
        if not codigo_fifa == None:
            if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3:
                raise ValueError("Error: código FIFA inválido o vacio, debe contener exactamente 3 caracteres")
            self.codigo_fifa = codigo_fifa
        
        if not nombre == None:
            if not isinstance(nombre, str) or nombre.strip() == "":
                raise ValueError("Error: nombre del país inválido o vacio")
            self.nombre = nombre
        
        if not continente == None:
            if not isinstance(continente, str) or continente.strip() == "":
                raise ValueError("Error: continente inválido o vacio")
            self.continente = continente
        
        if not ranking_fifa == None:
            if not isinstance(ranking_fifa, int) or ranking_fifa < 1 or ranking_fifa > 100:
                raise ValueError("Error: ranking FIFA debe ser un número entero positivo entre 1 y 100")
            self.ranking_fifa = ranking_fifa
"""
Nombre de clase: Seleccion
Entradas: codigo_equipo, pais, entrenador
Salidas: ninguna
Restricciones:
               codigo_equipo debe ser una cadena de texto no vacía
               pais debe ser una instancia de la clase Pais
               entrenador debe ser una instancia de la clase Entrenador
Función: representa una selección de fútbol, con atributos como código de equipo, país, entrenador, lista de jugadores y estadísticas del equipo, y funciones para mostrar datos, agregar o eliminar jugadores, asignar entrenador, registrar resultados y calcular la fuerza del equipo."""
class Seleccion():
    def __init__(self, codigo_equipo, pais, entrenador):
        if not isinstance(codigo_equipo, str) or codigo_equipo.strip() == "":
            raise ValueError("Error: código de equipo inválido o vacío")
        if not isinstance(pais, Pais):
            raise ValueError("Error: el país debe ser una instancia de la clase Pais")
        if not isinstance(entrenador, Entrenador):
            raise ValueError("Error: el entrenador debe ser una instancia de la clase Entrenador")
        
        self.codigo_equipo = codigo_equipo
        self.pais = pais
        self.entrenador = entrenador
        self.jugadores = []
        self.total_goles_favor = 0
        self.total_goles_contra = 0
        self.total_tarjetas_amarillas = 0
        self.total_tarjetas_rojas = 0
        self.fuerza_equipo = 0


    """
    Nombre: mostrar_datos
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: muestra los datos de la selección
    """
    def mostrar_datos(self):
        print(f"""Código de equipo: {self.codigo_equipo}
        País: {self.pais.nombre}
        Entrenador: {self.entrenador.nombre + " " + self.entrenador.apellido}
        Total goles a favor: {self.total_goles_favor}
        Total goles en contra: {self.total_goles_contra}
        Total tarjetas amarillas: {self.total_tarjetas_amarillas}
        Total tarjetas rojas: {self.total_tarjetas_rojas}
        Fuerza del equipo: {self.fuerza_equipo}""")
        print("Jugadores:")
        for jugador in self.jugadores:
            print(f" - {jugador.nombre} {jugador.apellido}, Posición: {jugador.posicion}, Dorsal: {jugador.dorsal}, Puntaje individual: {jugador.puntaje_individual}")

    """
    Nombre: agregar_jugador
    Entradas: futbolista
    Salidas: ninguna
    Restricciones: futbolista debe ser una instancia de la clase Futbolista y no puede haber más de 23 jugadores en la selección
    Función: agrega un jugador a la selección
    """
    def agregar_jugador(self, futbolista):

        if not isinstance(futbolista, Futbolista):
            raise ValueError("Error: el futbolista debe ser una instancia de la clase Futbolista")
        if len(self.jugadores) >= 23:
            raise ValueError("Error: no se pueden agregar más de 23 jugadores a la selección")
        
        for jugador in self.jugadores:
            if jugador.dorsal == futbolista.dorsal:
                raise ValueError("Error: ya existe un jugador con ese dorsal en la selección")
        
        self.jugadores = self.jugadores + [futbolista]

    """
    Nombre: eliminar_jugador
    Entradas: dorsal
    Salidas: ninguna
    Restricciones: dorsal debe ser un número entero positivo y existir en la lista de jugadores
    Función: elimina un jugador de la selección
    """
    def eliminar_jugador(self, dorsal):
        nueva_lista_jugadores = []
        jugador_encontrado = False 
        for jugador in self.jugadores:
            if jugador.dorsal == dorsal:
                jugador_encontrado = True
            else:
                nueva_lista_jugadores = nueva_lista_jugadores + [jugador]
        if not jugador_encontrado:
            raise ValueError("Error: no se encontró un jugador con ese dorsal en la selección")
        self.jugadores = nueva_lista_jugadores

    """
    Nombre: asignar_entrenador
    Entradas: entrenador
    Salidas: ninguna
    Restricciones: entrenador debe ser una instancia de la clase Entrenador
    Función: asigna un entrenador a la selección
    """
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador, Entrenador):
            raise ValueError("Error: el entrenador debe ser una instancia de la clase Entrenador")
        self.entrenador = entrenador

    """
    Nombre: registrar_resultado
    Entradas: goles_favor, goles_contra, tarjetas_amarillas, tarjetas_rojas
    Salidas: ninguna
    Restricciones: los parámetros deben cumplir con sus respectivas validaciones
    Función: registra los resultados de un partido
    """
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_amarillas, tarjetas_rojas):
        if not isinstance(goles_favor, int) or goles_favor < 0:
            raise ValueError("Error: los goles a favor deben ser un número entero no negativo")
        if not isinstance(goles_contra, int) or goles_contra < 0:
            raise ValueError("Error: los goles en contra deben ser un número entero no negativo")
        if not isinstance(tarjetas_amarillas, int) or tarjetas_amarillas < 0:
            raise ValueError("Error: las tarjetas amarillas deben ser un número entero no negativo")
        if not isinstance(tarjetas_rojas, int) or tarjetas_rojas < 0:
            raise ValueError("Error: las tarjetas rojas deben ser un número entero no negativo")
        
        self.total_goles_favor += goles_favor
        self.total_goles_contra += goles_contra
        self.total_tarjetas_amarillas += tarjetas_amarillas
        self.total_tarjetas_rojas += tarjetas_rojas
    """
    Nombre: calcular_fuerza_equipo
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: calcula la fuerza del equipo
    """
    def calcular_fuerza_equipo(self):
        if len(self.jugadores) == 0:
            self.fuerza_equipo = 0
            return
        
        candidatos = self.jugadores
        titulares = []
        
        cantidad_titulares = 11
        if len(self.jugadores) < 11:
            cantidad_titulares = len(self.jugadores)
        
        contador = 0
        # Se escogen a los mejores 11 jugadores para ser titulares, basandome en el puntaje individual de cada jugador y se van eliminando de la lista de candidatos para no volver a elegirlos
        while contador < cantidad_titulares:
            mejor_jugador = candidatos[0]
            for jugador in candidatos:
                if jugador.puntaje_individual > mejor_jugador.puntaje_individual:
                    mejor_jugador = jugador
            
            titulares = titulares + [mejor_jugador]
            
            nuevos_candidatos = []
            for jugador in candidatos:
                if jugador != mejor_jugador:
                    nuevos_candidatos = nuevos_candidatos + [jugador]
            candidatos = nuevos_candidatos
            
            contador += 1
        
        # Se calcula el promedio del puntaje individual de los jugadores titulares para contribuir al cálculo de la fuerza del equipo
        suma_puntajes = 0
        for jugador in titulares:
            suma_puntajes += jugador.puntaje_individual
        promedio_jugadores = suma_puntajes / len(titulares)
        
        factor_entrenador = self.entrenador.experiencia_años * 4
        if factor_entrenador > 100:
            factor_entrenador = 100
        
        factor_ranking = 100 - self.pais.ranking_fifa
        
        self.fuerza_equipo = (promedio_jugadores * 0.6) + (factor_entrenador * 0.25) + (factor_ranking * 0.15)


"""
Nombre de clase: Partido
Entradas: id_partido, equipo1, equipo2, fecha, fase
Salidas: ninguna
Restricciones:
               id_partido debe ser un número entero positivo
              equipo1 y equipo2 deben ser instancias de la clase Seleccion
               fecha debe ser una cadena de texto no vacía
               fase debe ser una cadena de texto no vacía
Función: representa un partido de fútbol entre dos selecciones, con atributos para almacenar el resultado del partido y un método para simular el resultado basado en la fuerza de los equipos.
"""
class Partido():
    def __init__(self, id_partido, equipo1, equipo2, fecha, fase):
        if not isinstance(id_partido, int) or id_partido <= 0:
            raise ValueError("Error: el ID del partido debe ser un número entero positivo")
        
        if not isinstance(equipo1, Seleccion):
            raise ValueError("Error: el equipo local debe ser una instancia de la clase Seleccion")
        if not isinstance(equipo2, Seleccion):
            raise ValueError("Error: el equipo visitante debe ser una instancia de la clase Seleccion")
        if not isinstance(fecha, str) or fecha.strip() == "":
            raise ValueError("Error: fecha inválida o vacia")
        if not isinstance(fase, str) or fase.strip() == "":
            raise ValueError("Error: fase inválida o vacia")

        self.id_partido = id_partido
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.fecha = fecha
        self.fase = fase   
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.penales_equipo1 = 0
        self.penales_equipo2 = 0
        self.gano_por_penales = False

    """
    Nombre: Simular
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: simula el resultado de un partido entre equipo1 y equipo2, asign
    """
    def Simular(self):
        diferencia = self.equipo1.fuerza_equipo - self.equipo2.fuerza_equipo
        diferencia_absoluta = diferencia


        if diferencia_absoluta < 0:
            # Si la diferencia es negativa, se convierte a positiva para evaluar los rangos
            diferencia_absoluta =  diferencia_absoluta * -1
        if diferencia_absoluta <= 15:
            # Diferencia de 15 puntos o menos, ambos equipos tienen una probabilidad similar de ganar
            self.goles_equipo1 = random.randint(0, 4)
            self.goles_equipo2 = random.randint(0, 4)

        elif diferencia_absoluta <= 30:
            # Diferencia entre 16 y 30 puntos, el equipo más fuerte tiene una probabilidad ligeramente mayor de ganar
            if diferencia > 0:
                # El equipo 1 es más fuerte, tiene un poco más probabilidades de ganar
                self.goles_equipo1 = random.randint(1, 5)
                self.goles_equipo2 = random.randint(0, 4)
            else:
                # El equipo 2 es más fuerte, tiene un poco más probabilidades de ganar
                self.goles_equipo1 = random.randint(0, 4)
                self.goles_equipo2 = random.randint(1, 5)

        else:
            # Diferencia mayor a 30 puntos, el equipo más fuerte tiene una probabilidad significativamente mayor de ganar
            if diferencia > 0:
                # El equipo 1 es más fuerte, tiene mas probabilidades de ganar
                self.goles_equipo1 = random.randint(2, 7)
                self.goles_equipo2 = random.randint(0, 3)
            else:
                # El equipo 2 es más fuerte, tiene mas probabilidades de ganar
                self.goles_equipo1 = random.randint(0, 3)
                self.goles_equipo2 = random.randint(2, 7)

        contador_goles1 = 0
        while contador_goles1 < self.goles_equipo1:
            jugador_random = random.choice(self.equipo1.jugadores)
            jugador_random.registrar_gol()
            contador_goles1 += 1
        
        contador_goles2 = 0
        while contador_goles2 < self.goles_equipo2:
            jugador_random = random.choice(self.equipo2.jugadores)
            jugador_random.registrar_gol()
            contador_goles2 += 1
        self.equipo1.registrar_resultado(self.goles_equipo1, self.goles_equipo2, 0, 0)
        self.equipo2.registrar_resultado(self.goles_equipo2, self.goles_equipo1, 0, 0)

    """
    Nombre: generar_ganador
    Entradas: ninguna
    Salidas: el equipo que ganó el partido
    Restricciones: ninguna
    Función: determina el equipo ganador del partido, considerando si se resolvió por penales o por goles
    """
    def generar_ganador(self):
        if self.gano_por_penales:
            if self.penales_equipo1 > self.penales_equipo2:
                return self.equipo1
            else:
                return self.equipo2
        
        if self.goles_equipo1 > self.goles_equipo2:
            return self.equipo1
        elif self.goles_equipo2 > self.goles_equipo1:
            return self.equipo2
        else:
            return None
    

    """
    Nombre: mostrar_resultado
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: muestra el resultado del partido en la consola
    """
    def mostrar_resultado(self):
        print(f"{self.equipo1.pais.nombre} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2.pais.nombre}")

"""
Nombre de clase: Grupo
Entradas: nombre_grupo
Salidas: ninguna
Restricciones: nombre_grupo debe ser una cadena de texto no vacía
Función: representa un grupo de la fase de grupos del Mundial, con atributos para almacenar los equipos del grupo y los partidos jugados, y funciones para agregar equipos al grupo y simular los partidos entre los equipos del grupo.
"""
class Grupo():
    def __init__(self, nombre_grupo):
        if not isinstance(nombre_grupo, str) or nombre_grupo.strip() == "":
            raise ValueError("Error: nombre del grupo inválido o vacio")
        self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []
    """
    Nombre: agregar_equipo
    Entradas: seleccion
    Salidas: ninguna
    Restricciones: se necesitan al menos 4 equipos en el grupo para agregar uno más
    Función: agrega un equipo al grupo si cumple con las restricciones, verificando que no se exceda el límite de equipos por grupo y que no haya equipos con el mismo código en el grupo
    """
    def agregar_equipo(self, seleccion):
        if not isinstance(seleccion, Seleccion):
            raise ValueError("Error: la selección debe ser una instancia de la clase Seleccion")
        if len(self.equipos) >= 4:
            raise ValueError("Error: no se pueden agregar más de 4 equipos a un grupo")
        
        for equipo in self.equipos:
            if equipo.codigo_equipo == seleccion.codigo_equipo:
                raise ValueError("Error: ya existe un equipo con ese código en el grupo")
        
        self.equipos = self.equipos + [seleccion]

    """
    Nombre: jugar_partidos
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: se necesitan al menos 2 equipos en el grupo para jugar partidos
    Función: simula los partidos entre los equipos del grupo, asignando fechas a cada partido y almacenando los resultados en la lista de partidos del grupo
    """
    def jugar_partidos(self):
        if len(self.equipos) < 2:
            raise ValueError("Error: se necesitan al menos 2 equipos para jugar partidos en el grupo")
        
        # Se asignan fechas a los partidos, comenzando desde el 11 de junio de 2026 y sumando un día para cada partido siguiente

        fecha_inicio = datetime.date(2026, 6, 11)
        
        # Se generan los partidos entre cada par de equipos en el grupo, asegurando que cada equipo juegue contra todos los demás equipos una vez
        id_partido = 1
        for i in range(len(self.equipos)):
            for j in range(i + 1, len(self.equipos)):
                dias_a_sumar = id_partido - 1
                fecha_partido = fecha_inicio + datetime.timedelta(days=dias_a_sumar)
                fecha_texto = fecha_partido.strftime("%d/%m/%Y")
                
                partido = Partido(id_partido, self.equipos[i], self.equipos[j], fecha_texto, self.nombre_grupo)
                partido.Simular()
                self.partidos = self.partidos + [partido]
                id_partido += 1


    """
    Nombre: calcular_tabla
    Entradas: ninguna
    Salidas: una lista con la tabla de posiciones del grupo, ordenada por puntos, diferencia de goles y goles a favor
    Restricciones: ninguna
    Función: calcula la tabla de posiciones del grupo, asignando puntos a cada equipo según los resultados de los partidos jugados, y ordenando la tabla por puntos, diferencia de goles y goles a favor
    """
    def calcular_tabla(self):
        tabla = []
        for equipo in self.equipos:
            puntos = 0
            goles_favor = 0
            goles_contra = 0
            
            for partido in self.partidos:
                if partido.equipo1 == equipo:
                    goles_favor += partido.goles_equipo1
                    goles_contra += partido.goles_equipo2
                    if partido.goles_equipo1 > partido.goles_equipo2:
                        puntos += 3
                    elif partido.goles_equipo1 == partido.goles_equipo2:
                        puntos += 1
                
                elif partido.equipo2 == equipo:
                    goles_favor += partido.goles_equipo2
                    goles_contra += partido.goles_equipo1
                    if partido.goles_equipo2 > partido.goles_equipo1:
                        puntos += 3
                    elif partido.goles_equipo2 == partido.goles_equipo1:
                        puntos += 1
            
            tabla = tabla + [(equipo, puntos, goles_favor, goles_contra)]
        
        # Se ordena la tabla por puntos, luego por diferencia de goles y finalmente por goles a favor
        n = len(tabla)
        for i in range(n):
            for j in range(n - 1 - i):
                actual = tabla[j]
                siguiente = tabla[j + 1]
                
                puntos_actual = actual[1]
                puntos_siguiente = siguiente[1]
                
                diferencia_actual = actual[2] - actual[3]
                diferencia_siguiente = siguiente[2] - siguiente[3]
                
                goles_favor_actual = actual[2]
                goles_favor_siguiente = siguiente[2]
                
                debe_intercambiar = False
                
                if puntos_actual < puntos_siguiente:
                    debe_intercambiar = True
                elif puntos_actual == puntos_siguiente:
                    if diferencia_actual < diferencia_siguiente:
                        debe_intercambiar = True
                    elif diferencia_actual == diferencia_siguiente:
                        if goles_favor_actual < goles_favor_siguiente:
                            debe_intercambiar = True
                
                if debe_intercambiar:
                    tabla[j] = siguiente
                    tabla[j + 1] = actual      
        return tabla
            
    
    """
    Nombre: obtener_clasificados
    Entradas: ninguna
    Salidas: una tupla con los dos equipos clasificados del grupo
    Restricciones: se necesitan al menos 2 equipos en el grupo para determinar la clasificación
    Función: obtiene los dos equipos clasificados del grupo, basándose en la tabla de posiciones calculada, y devolviendo el primer y segundo lugar del grupo
    """
    def obtener_clasificados(self):
        tabla = self.calcular_tabla()
        
        if len(tabla) < 2:
            raise ValueError("Error: no hay suficientes equipos en el grupo para determinar la clasificación")
        primer_lugar = tabla[0][0]
        segundo_lugar = tabla[1][0] 

        return primer_lugar, segundo_lugar

    """
    Nombre: mostrar_tabla
    Entradas: ninguna
    Salidas: ninguna
    Restricciones: ninguna
    Función: muestra la tabla de posiciones del grupo en la consola, mostrando el nombre del equipo, puntos, goles a favor y goles en contra
    """
    def mostrar_tabla(self):
        tabla = self.calcular_tabla()
        print(f"Tabla del Grupo {self.nombre_grupo}:")
        print("Equipo\tPuntos\tGoles a favor\tGoles en contra")
        for info in tabla:
            equipo = info[0]
            puntos = info[1]
            goles_favor = info[2]
            goles_contra = info[3]
            print(f"{equipo.pais.nombre}\t{puntos}\t{goles_favor}\t{goles_contra}")

"""
Nombre de clase: Fase
Entradas: nombre_fase
Salidas: ninguna
Restricciones: nombre_fase debe ser una cadena de texto no vacía
Función: representa una fase del Mundial, como octavos de final, cuartos de final, semifinales o final, con atributos para almacenar los partidos de la fase y funciones para registrar juegos, simular la fase, mostrar los juegos y obtener los equipos clasificados a la siguiente fase.
"""
class Fase():
    def __init__(self, nombre_fase):
        if not isinstance(nombre_fase, str) or nombre_fase.strip() == "":
            raise ValueError("Error: nombre de la fase inválido o vacio")
        self.nombre_fase = nombre_fase
        self.partidos = []
    """
    Nombre: registrar_juego
    Entradas: equipo1, equipo2
    Salidas: ninguna
    Restricciones: equipo1 y equipo2 deben ser instancias de la clase Seleccion
    Función: registra un juego entre dos equipos en la fase, asignando un ID al partido y una fecha basada en el orden de registro de los partidos, y almacenando el partido en la lista de partidos de la fase
    """
    def registrar_juego(self, equipo1, equipo2):
        if not isinstance(equipo1, Seleccion):
            raise ValueError("Error: el equipo local debe ser una instancia de la clase Seleccion")
        if not isinstance(equipo2, Seleccion):
            raise ValueError("Error: el equipo visitante debe ser una instancia de la clase Seleccion")
        
        id_partido = len(self.partidos) + 1
        fecha_inicio = datetime.date(2026, 6, 11)
        dias_a_sumar = id_partido - 1
        fecha_partido = fecha_inicio + datetime.timedelta(days=dias_a_sumar)
        fecha_texto = fecha_partido.strftime("%d/%m/%Y")

        partido = Partido(id_partido, equipo1, equipo2, fecha_texto, self.nombre_fase)
        self.partidos = self.partidos + [partido]

    def jugar_fase(self):
        if len(self.partidos) == 0:
            raise ValueError("Error: no hay partidos registrados en esta fase para jugar")
        
        for partido in self.partidos:
            partido.Simular()     

            if partido.goles_equipo1 == partido.goles_equipo2:
                penales1 = random.randint(2, 5)
                penales2 = random.randint(2, 5)
                while penales1 == penales2:
                    penales1 = random.randint(2, 5)
                    penales2 = random.randint(2, 5)
                
                partido.penales_equipo1 = penales1
                partido.penales_equipo2 = penales2
                partido.gano_por_penales = True
            else: 
                partido.gano_por_penales = False

    def mostrar_juegos(self):
        if len(self.partidos) == 0:
            print("No hay partidos registrados en esta fase.")
            return
        
        print(f"Partidos de la fase {self.nombre_fase}:")
        for partido in self.partidos:
            resultado = f"{partido.equipo1.pais.nombre} {partido.goles_equipo1} - {partido.goles_equipo2} {partido.equipo2.pais.nombre}"
            if partido.gano_por_penales:
                resultado += f" (Penales: {partido.penales_equipo1} - {partido.penales_equipo2})"
            print(resultado)

    def obtener_clasificados(self):
        clasificados = []
        for partido in self.partidos:
            ganador = partido.generar_ganador()
            clasificados = clasificados + [ganador]
        return clasificados

class Mundial():
    def __init__(self, nombre, año):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("Error: nombre del mundial inválido o vacio")
        if not isinstance(año, int) or año < 1900:
            raise ValueError("Error: año del mundial debe ser un número entero mayor o igual a 1900")
        self.nombre = nombre
        self.año = año
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    def registrar_pais(self, pais):
        if not isinstance(pais, Pais):
            raise ValueError("Error: el país debe ser una instancia de la clase Pais")
        for p in self.paises:
            if p.codigo_fifa == pais.codigo_fifa:
                raise ValueError("Error: ya existe un país con ese código FIFA registrado en el mundial")
        self.paises = self.paises + [pais]

    def registrar_seleccion(self, seleccion):
        if not isinstance(seleccion, Seleccion):
            raise ValueError("Error: la selección debe ser una instancia de la clase Seleccion")
        for s in self.selecciones:
            if s.codigo_equipo == seleccion.codigo_equipo:
                raise ValueError("Error: ya existe una selección con ese código de equipo registrado en el mundial")
        self.selecciones = self.selecciones + [seleccion]

    def crear_grupos(self, cantidad_grupos):
        if not isinstance(cantidad_grupos, int) or cantidad_grupos < 2:
            raise ValueError("Error: la cantidad de grupos debe ser un número entero mayor o igual a 2")
        
        selecciones_necesarias = cantidad_grupos * 4
        if len(self.selecciones) != selecciones_necesarias:
            raise ValueError(f"Error: se necesitan exactamente {selecciones_necesarias} selecciones registradas para crear {cantidad_grupos} grupos")
        
        self.grupos = []
        for i in range(cantidad_grupos):
            nombre_grupo = "Grupo " + chr(65 + i)
            grupo = Grupo(nombre_grupo)
            self.grupos = self.grupos + [grupo]
        
        indice_seleccion = 0
        for seleccion in self.selecciones:
            indice_grupo = indice_seleccion % cantidad_grupos
            self.grupos[indice_grupo].agregar_equipo(seleccion)
            indice_seleccion += 1

    def jugar_fase_grupos(self):
        if len(self.grupos) == 0:
            raise ValueError("Error: no hay grupos creados para jugar la fase de grupos")
        
        for grupo in self.grupos:
            grupo.jugar_partidos()

    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        if not isinstance(nombre_fase, str) or nombre_fase.strip() == "":
            raise ValueError("Error: nombre de la fase inválido o vacio")
        if not isinstance(clasificados, list) or len(clasificados) == 0:
            raise ValueError("Error: la lista de clasificados debe ser una lista no vacía de selecciones")
        
        fase = Fase(nombre_fase)
        for i in range(0, len(clasificados), 2):
            equipo1 = clasificados[i]
            equipo2 = clasificados[i + 1]
            fase.registrar_juego(equipo1, equipo2)
        
        self.fases = self.fases + [fase]
        return fase
    

    def jugar_fase_eliminatoria(self, fase):
        if not isinstance(fase, Fase):
            raise ValueError("Error: la fase debe ser una instancia de la clase Fase")
        fase.jugar_fase()
        clasificados = fase.obtener_clasificados()
        return clasificados
    
    def determinar_campeon(self):
        if len(self.grupos) == 0:
            raise ValueError("Error: no hay grupos creados para determinar el campeón")
        
        clasificados = []
        for grupo in self.grupos:
            primer_lugar, segundo_lugar = grupo.obtener_clasificados()
            clasificados = clasificados + [primer_lugar, segundo_lugar]
        
        while len(clasificados) > 1:
            cantidad_equipos = len(clasificados)

            if cantidad_equipos == 16:
                nombre_fase = "Octavos de final"
            elif cantidad_equipos == 8:
                nombre_fase = "Cuartos de final"
            elif cantidad_equipos == 4:
                nombre_fase = "Semifinales"
            elif cantidad_equipos == 2:
                nombre_fase = "Final"
            else:
                nombre_fase = f"Fase con {cantidad_equipos} equipos"

            fase = self.armar_fase_eliminatoria(nombre_fase, clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        self.campeon = clasificados[0]

    def mostrar_tabla_general(self):
        print(f"Tabla general del Mundial {self.nombre} {self.año}:")
        for grupo in self.grupos:
            grupo.mostrar_tabla()

    def generar_reporte(self):
        print(f"Reporte del Mundial {self.nombre} {self.año}:")
        print("Grupos y clasificados:")
        for grupo in self.grupos:
            primer_lugar, segundo_lugar = grupo.obtener_clasificados()
            print(f"{grupo.nombre_grupo}: 1er lugar - {primer_lugar.pais.nombre}, 2do lugar - {segundo_lugar.pais.nombre}")
        
        print("\nFases eliminatorias:")
        for fase in self.fases:
            print(f"Fase: {fase.nombre_fase}")
            for partido in fase.partidos:
                resultado = f"{partido.equipo1.pais.nombre} {partido.goles_equipo1} - {partido.goles_equipo2} {partido.equipo2.pais.nombre}"
                if partido.gano_por_penales:
                    resultado += f" (Penales: {partido.penales_equipo1} - {partido.penales_equipo2})"
                print(resultado)
        
        if self.campeon:
            print(f"\nCampeón del Mundial: {self.campeon.pais.nombre}")
        else:
            print("\nNo se ha determinado un campeón aún.")
        
        # Ranking de goleadores
        todos_los_jugadores = []
        for seleccion in self.selecciones:
            for jugador in seleccion.jugadores:
                todos_los_jugadores = todos_los_jugadores + [jugador]
        
        n = len(todos_los_jugadores)
        for i in range(n):
            for j in range(n - 1 - i):
                if todos_los_jugadores[j].goles < todos_los_jugadores[j + 1].goles:
                    temporal = todos_los_jugadores[j]
                    todos_los_jugadores[j] = todos_los_jugadores[j + 1]
                    todos_los_jugadores[j + 1] = temporal
        
        archivo_goleadores = open("ranking_goleadores.txt", "w", encoding="utf-8")
        for jugador in todos_los_jugadores:
            linea = f"{jugador.nombre} {jugador.apellido},{jugador.nacionalidad},{jugador.goles}\n"
            archivo_goleadores.write(linea)
        archivo_goleadores.close()
        
        print("\nArchivo ranking_goleadores.txt generado correctamente")

        selecciones_ordenadas = self.selecciones
        n = len(selecciones_ordenadas)
        for i in range(n):
            for j in range(n - 1 - i):
                diferencia_actual = selecciones_ordenadas[j].total_goles_favor - selecciones_ordenadas[j].total_goles_contra
                diferencia_siguiente = selecciones_ordenadas[j + 1].total_goles_favor - selecciones_ordenadas[j + 1].total_goles_contra
                        
                if diferencia_actual < diferencia_siguiente:
                    temporal = selecciones_ordenadas[j]
                    selecciones_ordenadas[j] = selecciones_ordenadas[j + 1]
                    selecciones_ordenadas[j + 1] = temporal

        archivo_selecciones = open("ranking_selecciones.txt", "w", encoding="utf-8")
        for seleccion in selecciones_ordenadas:
            diferencia = seleccion.total_goles_favor - seleccion.total_goles_contra
            linea = f"{seleccion.pais.nombre},{seleccion.total_goles_favor},{seleccion.total_goles_contra},{diferencia}\n"
            archivo_selecciones.write(linea)
        archivo_selecciones.close()
        print("\nArchivo ranking_selecciones.txt generado correctamente")

    def guardar_paises(self):
        archivo_paises = open("paises.txt", "w", encoding="utf-8")
        for pais in self.paises:
            linea = f"{pais.codigo_fifa},{pais.nombre},{pais.continente},{pais.ranking_fifa}\n"
            archivo_paises.write(linea)
        archivo_paises.close()
        print("\nArchivo paises.txt generado correctamente")

    def cargar_paises(self):
        try:
            archivo_paises = open("paises.txt", "r", encoding="utf-8")
            lineas = archivo_paises.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    
                    try:
                        ranking_fifa = int(datos[3])
                        pais = Pais(datos[0], datos[1], datos[2], ranking_fifa)
                        self.registrar_pais(pais)
                    except ValueError:
                        print(f"Error: el ranking FIFA debe ser un número entero en la línea: {linea.strip()}")
                else:
                    print(f"Error: formato incorrecto en la línea: {linea.strip()}")
            archivo_paises.close()
            print("\nPaises cargados correctamente desde paises.txt")
        except FileNotFoundError:
            print("Archivo paises.txt no encontrado. No se han cargado países.")
    
    def guardar_selecciones(self):
        archivo_selecciones = open("selecciones.txt", "w", encoding="utf-8")
        for seleccion in self.selecciones:
            entrenador = seleccion.entrenador
            linea = f"{seleccion.codigo_equipo},{seleccion.pais.codigo_fifa},{entrenador.nombre},{entrenador.apellido},{entrenador.fecha_nacimiento},{entrenador.nacionalidad},{entrenador.licencia},{entrenador.experiencia_años},{entrenador.sistema_juego}\n"
            archivo_selecciones.write(linea)
        archivo_selecciones.close()
        print("\nArchivo selecciones.txt generado correctamente")

    def cargar_selecciones(self):
        try:
            archivo_selecciones = open("selecciones.txt", "r", encoding="utf-8")
            lineas = archivo_selecciones.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) == 9:
                    codigo_equipo = datos[0]
                    codigo_fifa = datos[1]
                    entrenador_nombre = datos[2]
                    entrenador_apellido = datos[3]
                    entrenador_fecha_nacimiento = datos[4]
                    entrenador_nacionalidad = datos[5]
                    entrenador_licencia = datos[6]
                    entrenador_experiencia_años = int(datos[7])
                    entrenador_sistema_juego = datos[8]
                    
                    pais_encontrado = None
                    for pais in self.paises:
                        if pais.codigo_fifa == codigo_fifa:
                            pais_encontrado = pais
                            break
                    
                    if pais_encontrado is not None:
                        entrenador = Entrenador(entrenador_nombre, entrenador_apellido, entrenador_fecha_nacimiento, entrenador_nacionalidad, entrenador_licencia, entrenador_experiencia_años, entrenador_sistema_juego)
                        seleccion = Seleccion(codigo_equipo, pais_encontrado, entrenador)
                        self.registrar_seleccion(seleccion)
                    else:
                        print(f"Error: no se encontró un país con el código FIFA {codigo_fifa} para la selección con código de equipo {codigo_equipo}")
                else:
                    print(f"Error: formato incorrecto en la línea: {linea.strip()}")
            archivo_selecciones.close()
            print("\nSelecciones cargadas correctamente desde selecciones.txt")
        except FileNotFoundError:
            print("Archivo selecciones.txt no encontrado. No se han cargado selecciones.")
    

    def guardar_jugadores(self):
        archivo_jugadores = open("jugadores.txt", "w", encoding="utf-8")
        for seleccion in self.selecciones:
            for jugador in seleccion.jugadores:
                linea = f"{jugador.nombre},{jugador.apellido},{jugador.fecha_nacimiento},{jugador.nacionalidad},{jugador.posicion},{jugador.dorsal},{jugador.puntaje_individual},{jugador.goles},{jugador.asistencias},{jugador.total_tarjetas_amarillas},{jugador.total_tarjetas_rojas},{seleccion.codigo_equipo}\n"
                archivo_jugadores.write(linea)
        archivo_jugadores.close()
        print("\nArchivo jugadores.txt generado correctamente")

    def cargar_jugadores(self):
        try:
            archivo_jugadores = open("jugadores.txt", "r", encoding="utf-8")
            lineas = archivo_jugadores.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) == 12:
                    nombre = datos[0]
                    apellido = datos[1]
                    fecha_nacimiento = datos[2]
                    nacionalidad = datos[3]
                    posicion = datos[4]
                    dorsal = int(datos[5])
                    puntaje_individual = int(datos[6])
                    goles_guardados = int(datos[7])
                    asistencias_guardadas = int(datos[8])
                    amarillas_guardadas = int(datos[9])
                    rojas_guardadas = int(datos[10])
                    codigo_equipo_buscado = datos[11]
                    
                    seleccion_encontrada = None
                    for seleccion in self.selecciones:
                        if seleccion.codigo_equipo == codigo_equipo_buscado:
                            seleccion_encontrada = seleccion
                            break
                    
                    if seleccion_encontrada is not None:
                        jugador = Futbolista(nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual)
                        
                        contador_goles = 0
                        while contador_goles < goles_guardados:
                            jugador.registrar_gol()
                            contador_goles += 1
                        
                        contador_asistencias = 0
                        while contador_asistencias < asistencias_guardadas:
                            jugador.registrar_asistencia()
                            contador_asistencias += 1
                        
                        contador_amarillas = 0
                        while contador_amarillas < amarillas_guardadas:
                            jugador.registrar_tarjeta("amarilla")
                            contador_amarillas += 1
                        
                        contador_rojas = 0
                        while contador_rojas < rojas_guardadas:
                            jugador.registrar_tarjeta("roja")
                            contador_rojas += 1
                        
                        seleccion_encontrada.agregar_jugador(jugador)
                    else:
                        print(f"Error: no se encontró la selección con código {codigo_equipo_buscado} para el jugador {nombre} {apellido}")
                else:
                    print(f"Error: formato incorrecto en la línea: {linea.strip()}")
            archivo_jugadores.close()
            print("\nJugadores cargados correctamente desde jugadores.txt")
        except FileNotFoundError:
            print("Archivo jugadores.txt no encontrado. No se han cargado jugadores.")
        
    def guardar_partidos(self):
        archivo_partidos = open("partidos.txt", "w", encoding="utf-8")
        
        for grupo in self.grupos:
            for partido in grupo.partidos:
                linea = f"{partido.id_partido},{partido.equipo1.pais.nombre},{partido.equipo2.pais.nombre},{partido.goles_equipo1},{partido.goles_equipo2},{partido.fecha},{partido.fase}\n"
                archivo_partidos.write(linea)
        
        for fase in self.fases:
            for partido in fase.partidos:
                linea = f"{partido.id_partido},{partido.equipo1.pais.nombre},{partido.equipo2.pais.nombre},{partido.goles_equipo1},{partido.goles_equipo2},{partido.fecha},{partido.fase}\n"
                archivo_partidos.write(linea)
        
        archivo_partidos.close()
        print("\nArchivo partidos.txt generado correctamente")

    def cargar_partidos(self):
        try:
            archivo_partidos = open("partidos.txt", "r", encoding="utf-8")
            lineas = archivo_partidos.readlines()
            
            print("\nPartidos cargados desde partidos.txt:")
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) == 7:
                    id_partido = datos[0]
                    nombre_equipo1 = datos[1]
                    nombre_equipo2 = datos[2]
                    goles_equipo1 = datos[3]
                    goles_equipo2 = datos[4]
                    fecha = datos[5]
                    fase_nombre = datos[6]
                    
                    print(f"Partido #{id_partido} ({fase_nombre}, {fecha}): {nombre_equipo1} {goles_equipo1} - {goles_equipo2} {nombre_equipo2}")
                else:
                    print(f"Error: formato incorrecto en la línea: {linea.strip()}")
            
            archivo_partidos.close()
        except FileNotFoundError:
            print("Archivo partidos.txt no encontrado. No se han cargado partidos.")
