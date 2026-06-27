import random
import datetime
import tkinter as tk


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
            
        amarillas1 = random.randint(0, 3)
        rojas1 = random.randint(0, 1)
        for _ in range(amarillas1):
            random.choice(self.equipo1.jugadores).registrar_tarjeta("amarilla")
        for _ in range(rojas1):
            random.choice(self.equipo1.jugadores).registrar_tarjeta("roja")

        amarillas2 = random.randint(0, 3)
        rojas2 = random.randint(0, 1)
        for _ in range(amarillas2):
            random.choice(self.equipo2.jugadores).registrar_tarjeta("amarilla")
        for _ in range(rojas2):
            random.choice(self.equipo2.jugadores).registrar_tarjeta("roja")

        self.equipo1.registrar_resultado(self.goles_equipo1, self.goles_equipo2, amarillas1, rojas1)
        self.equipo2.registrar_resultado(self.goles_equipo2, self.goles_equipo1, amarillas2, rojas2)
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
            linea = f"{seleccion.pais.nombre};{seleccion.total_goles_favor};{seleccion.total_goles_contra};{diferencia}\n"
            archivo_selecciones.write(linea)
        archivo_selecciones.close()
        print("\nArchivo ranking_selecciones.txt generado correctamente")

    def guardar_paises(self):
        archivo_paises = open("paises.txt", "w", encoding="utf-8")
        for pais in self.paises:
            linea = f"{pais.codigo_fifa};{pais.nombre};{pais.continente};{pais.ranking_fifa}\n"
            archivo_paises.write(linea)
        archivo_paises.close()
        print("\nArchivo paises.txt generado correctamente")

    def cargar_paises(self):
        try:
            archivo_paises = open("paises.txt", "r", encoding="utf-8")
            lineas = archivo_paises.readlines()
            for linea in lineas:
                datos = linea.strip().split(";")
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
            print("Archivo paises.txt no encontrado. No se han cargado paises.")
    
    def guardar_selecciones(self):
        archivo_selecciones = open("selecciones.txt", "w", encoding="utf-8")
        for seleccion in self.selecciones:
            entrenador = seleccion.entrenador
            linea = f"{seleccion.codigo_equipo};{seleccion.pais.codigo_fifa};{entrenador.nombre};{entrenador.apellido};{entrenador.fecha_nacimiento};{entrenador.nacionalidad};{entrenador.licencia};{entrenador.experiencia_años};{entrenador.sistema_juego}\n"
            archivo_selecciones.write(linea)
        archivo_selecciones.close()
        print("\nArchivo selecciones.txt generado correctamente")

    def cargar_selecciones(self):
        try:
            archivo_selecciones = open("selecciones.txt", "r", encoding="utf-8")
            lineas = archivo_selecciones.readlines()
            for linea in lineas:
                datos = linea.strip().split(";")
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
                    
                    if not pais_encontrado == None:
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
                linea = f"{jugador.nombre};{jugador.apellido};{jugador.fecha_nacimiento};{jugador.nacionalidad};{jugador.posicion};{jugador.dorsal};{jugador.puntaje_individual};{jugador.goles};{jugador.asistencias};{jugador.total_tarjetas_amarillas};{jugador.total_tarjetas_rojas};{seleccion.codigo_equipo}\n"
                archivo_jugadores.write(linea)
        archivo_jugadores.close()
        print("\nArchivo jugadores.txt generado correctamente")

    def cargar_jugadores(self):
        try:
            archivo_jugadores = open("jugadores.txt", "r", encoding="utf-8")
            lineas = archivo_jugadores.readlines()
            for linea in lineas:
                datos = linea.strip().split(";")
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
                    
                    if not seleccion_encontrada == None:
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
                linea = f"{partido.id_partido};{partido.equipo1.pais.nombre};{partido.equipo2.pais.nombre};{partido.goles_equipo1};{partido.goles_equipo2};{partido.fecha};{partido.fase}\n"
                archivo_partidos.write(linea)
        
        for fase in self.fases:
            for partido in fase.partidos:
                linea = f"{partido.id_partido};{partido.equipo1.pais.nombre};{partido.equipo2.pais.nombre};{partido.goles_equipo1};{partido.goles_equipo2};{partido.fecha};{partido.fase}\n"
                archivo_partidos.write(linea)
        
        archivo_partidos.close()
        print("\nArchivo partidos.txt generado correctamente")

    def cargar_partidos(self):
        try:
            archivo_partidos = open("partidos.txt", "r", encoding="utf-8")
            lineas = archivo_partidos.readlines()
            
            print("\nPartidos cargados desde partidos.txt:")
            for linea in lineas:
                datos = linea.strip().split(";")
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


from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

"""
    Descripción:
    Crea un botón con el texto "Regresar" que permite cerrar la ventana actual y volver a la ventana anterior.
    Entradas:
    ventana: ventana (Tk o Toplevel) donde se colocará el botón.
    Salidas:
    No retorna ningún valor. Agrega un botón a la ventana.
    Restricciones:
    El parámetro ventana debe ser una ventana válida de Tkinter (Tk o Toplevel).
"""
def boton_regresar(ventana):

    btn_regresar = tk.Button(
        ventana,
        text="Regresar",
        width=15,
        bg="red",
        fg="white",
        font=("Arial", 10, "bold"),
        command=ventana.destroy
    )

    btn_regresar.pack(pady=10)

mundial = Mundial("FIFA", 2026)

mundial.cargar_paises()
mundial.cargar_selecciones()
mundial.cargar_jugadores()

print("Países:", len(mundial.paises))
print("Selecciones:", len(mundial.selecciones))
print("Jugadores:", len(mundial.selecciones))

ventana = tk.Tk()
ventana.title("Mundial FIFA 2026")
ventana.geometry("1000x600")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#222222",
    foreground="white",
    rowheight=28,
    fieldbackground="#222222",
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background="#1E88E5",
    foreground="white",
    font=("Arial", 11, "bold")
)

imagen = Image.open(
    "C:/Users/1002000016/OneDrive/Pictures/Screenshots/Proyecto3.mundial/proyecto3/imagensita.png"
)
imagen = imagen.resize((1000, 600))
imagen = ImageTk.PhotoImage(imagen)

fondo = tk.Label(ventana, image=imagen)
fondo.image = imagen
fondo.place(x=0, y=0, relwidth=1, relheight=1)

titulo = tk.Label(
    ventana,
    text="MUNDIAL FIFA 2026",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#000000"
)
titulo.place(relx=0.5, y=30, anchor="n")

"""
    Descripción:
    Abre una ventana con el menú de administración de países y selecciones, permitiendo acceder a las opciones de registrar un país, crear una selección y visualizar los países y selecciones registradas.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Muestra una ventana con las opciones del menú.
    Restricciones:
    Las funciones registrar_pais, crear_seleccion y ver_paises_selecciones deben existir previamente.
"""
def openPaises():

    menu = tk.Toplevel()
    menu.title("Países y Selecciones")
    menu.geometry("1920x1080")
    menu.configure(bg="#0f172a")

    tk.Label(
        menu,
        text="ADMINISTRAR\nPAÍSES Y SELECCIONES",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=25)

    frame_opciones = tk.Frame(menu, bg="#111827", padx=30, pady=25)
    frame_opciones.pack(pady=10)

    def boton_menu(texto, comando):
        tk.Button(
            frame_opciones,
            text=texto,
            font=("Arial", 13, "bold"),
            fg="white",
            bg="#111111",
            activebackground="#1E88E5",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=38,
            height=2,
            cursor="hand2",
            command=comando
        ).pack(pady=8)

    boton_menu("Registrar nuevo país", registrar_pais)
    boton_menu("Crear selección asociada a un país", crear_seleccion)
    boton_menu("Ver países y selecciones", ver_paises_selecciones)

    tk.Button(
        menu,
        text="Regresar",
        font=("Arial", 11, "bold"),
        fg="white",
        bg="#7f1d1d",
        activebackground="#dc2626",
        activeforeground="white",
        relief="flat",
        bd=0,
        width=25,
        cursor="hand2",
        command=menu.destroy
    ).pack(pady=15)

"""
    Descripción:
    Abre una ventana con un formulario para registrar un nuevo país, solicitando el código FIFA, nombre, continente y ranking FIFA. Al guardar, registra el país en el Mundial y almacena la información en el archivo correspondiente.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Agrega un nuevo país al Mundial y actualiza el archivo de países.
    Restricciones:
    Los datos ingresados deben cumplir las validaciones de la clase Pais y no puede existir otro país con el mismo código FIFA.
"""

def registrar_pais():

    ventana_pais = tk.Toplevel()
    ventana_pais.title("Registrar nuevo país")
    ventana_pais.geometry("1920x1080")
    ventana_pais.configure(bg="#0f172a")

    tk.Label(
        ventana_pais,
        text="Registrar nuevo país",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=15)

    tk.Label(ventana_pais, text="Código FIFA", bg="#0f172a", fg="white").pack()
    entrada_codigo = tk.Entry(ventana_pais)
    entrada_codigo.pack()

    tk.Label(ventana_pais, text="Nombre", bg="#0f172a", fg="white").pack()
    entrada_nombre = tk.Entry(ventana_pais)
    entrada_nombre.pack()

    tk.Label(ventana_pais, text="Continente", bg="#0f172a", fg="white").pack()
    entrada_continente = tk.Entry(ventana_pais)
    entrada_continente.pack()

    tk.Label(ventana_pais, text="Ranking FIFA", bg="#0f172a", fg="white").pack()
    entrada_ranking = tk.Entry(ventana_pais)
    entrada_ranking.pack()

    def guardar():
        try:
            pais = Pais(
                entrada_codigo.get().upper(),
                entrada_nombre.get(),
                entrada_continente.get(),
                int(entrada_ranking.get())
            )

            mundial.registrar_pais(pais)
            mundial.guardar_paises()

            messagebox.showinfo("Éxito", "País guardado correctamente.")

            entrada_codigo.delete(0, tk.END)
            entrada_nombre.delete(0, tk.END)
            entrada_continente.delete(0, tk.END)
            entrada_ranking.delete(0, tk.END)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventana_pais,
        text="Guardar país",
        width=25,
        bg="#111111",
        fg="white",
        command=guardar
    ).pack(pady=20)

    boton_regresar(ventana_pais)

"""
    Descripción:
    Abre una ventana para crear una selección asociada a un país registrado, permitiendo ingresar el código del equipo y los datos del entrenador. Al guardar, registra la selección y la almacena en el archivo correspondiente.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Registra una nueva selección en el Mundial y actualiza el archivo de selecciones.
    Restricciones:
    Debe existir al menos un país registrado, se debe seleccionar un país válido y los datos ingresados deben cumplir las validaciones de las clases Entrenador y Seleccion.
"""
    
def crear_seleccion():

    if len(mundial.paises) == 0:
        messagebox.showerror("Error", "Primero debe registrar al menos un país.")
        return

    ventana_sel = tk.Toplevel()
    ventana_sel.title("Crear selección asociada a un país")
    ventana_sel.geometry("1920x1080")
    ventana_sel.configure(bg="#0f172a")

    tk.Label(
        ventana_sel,
        text="Crear selección asociada a un país",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=15)

    tk.Label(ventana_sel, text="Código de equipo", bg="#0f172a", fg="white").pack()
    entrada_codigo = tk.Entry(ventana_sel)
    entrada_codigo.pack()

    nombres_paises = []
    for pais in mundial.paises:
        nombres_paises = nombres_paises + [pais.nombre]

    tk.Label(ventana_sel, text="País", bg="#0f172a", fg="white").pack()
    combo_pais = ttk.Combobox(ventana_sel, values=nombres_paises, state="readonly")
    combo_pais.pack()

    tk.Label(
        ventana_sel,
        text="Datos del entrenador",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=10)

    tk.Label(ventana_sel, text="Nombre", bg="#0f172a", fg="white").pack()
    entrada_nombre = tk.Entry(ventana_sel)
    entrada_nombre.pack()

    tk.Label(ventana_sel, text="Apellido", bg="#0f172a", fg="white").pack()
    entrada_apellido = tk.Entry(ventana_sel)
    entrada_apellido.pack()

    tk.Label(ventana_sel, text="Fecha nacimiento", bg="#0f172a", fg="white").pack()
    entrada_fecha = tk.Entry(ventana_sel)
    entrada_fecha.pack()

    tk.Label(ventana_sel, text="Nacionalidad", bg="#0f172a", fg="white").pack()
    entrada_nacionalidad = tk.Entry(ventana_sel)
    entrada_nacionalidad.pack()

    tk.Label(ventana_sel, text="Licencia", bg="#0f172a", fg="white").pack()
    entrada_licencia = tk.Entry(ventana_sel)
    entrada_licencia.pack()

    tk.Label(ventana_sel, text="Experiencia años", bg="#0f172a", fg="white").pack()
    entrada_experiencia = tk.Entry(ventana_sel)
    entrada_experiencia.pack()

    tk.Label(ventana_sel, text="Sistema de juego", bg="#0f172a", fg="white").pack()
    entrada_sistema = tk.Entry(ventana_sel)
    entrada_sistema.pack()

    def guardar():
        try:
            if combo_pais.current() == -1:
                messagebox.showerror("Error", "Debe seleccionar un país.")
                return

            pais = mundial.paises[combo_pais.current()]

            entrenador = Entrenador(
                entrada_nombre.get(),
                entrada_apellido.get(),
                entrada_fecha.get(),
                entrada_nacionalidad.get(),
                entrada_licencia.get(),
                int(entrada_experiencia.get()),
                entrada_sistema.get()
            )

            seleccion = Seleccion(
                entrada_codigo.get(),
                pais,
                entrenador
            )

            mundial.registrar_seleccion(seleccion)
            mundial.guardar_selecciones()

            messagebox.showinfo("Éxito", "Selección creada correctamente.")
            ventana_sel.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventana_sel,
        text="Guardar selección",
        width=25,
        bg="#111111",
        fg="white",
        command=guardar
    ).pack(pady=20)

    boton_regresar(ventana_sel)

"""
    Descripción:
    Abre una ventana con pestañas para mostrar los países y selecciones registradas, permitiendo actualizar los datos de un país o una selección seleccionada.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Muestra tablas con países y selecciones, y permite modificar datos existentes.
    Restricciones:
    Deben existir países o selecciones registradas para visualizar o actualizar datos. Para actualizar, el usuario debe seleccionar un elemento válido de la tabla.
"""

def ver_paises_selecciones():

    ventana_lista = tk.Toplevel()
    ventana_lista.title("Países y selecciones registradas")
    ventana_lista.geometry("1920x1080")

    notebook = ttk.Notebook(ventana_lista)
    notebook.pack(fill="both", expand=True)

    frame_paises = tk.Frame(notebook)
    frame_selecciones = tk.Frame(notebook)

    notebook.add(frame_paises, text="Países")
    notebook.add(frame_selecciones, text="Selecciones")

    tabla_paises = ttk.Treeview(
        frame_paises,
        columns=("codigo", "nombre", "continente", "ranking"),
        show="headings"
    )

    tabla_paises.heading("codigo", text="Código FIFA")
    tabla_paises.heading("nombre", text="País")
    tabla_paises.heading("continente", text="Continente")
    tabla_paises.heading("ranking", text="Ranking FIFA")

    tabla_paises.pack(fill="both", expand=True, padx=10, pady=10)

    for pais in mundial.paises:
        tabla_paises.insert(
            "",
            tk.END,
            values=(pais.codigo_fifa, pais.nombre, pais.continente, pais.ranking_fifa)
        )

    tabla_selecciones = ttk.Treeview(
        frame_selecciones,
        columns=("codigo", "pais", "entrenador", "jugadores"),
        show="headings"
    )

    tabla_selecciones.heading("codigo", text="Código equipo")
    tabla_selecciones.heading("pais", text="País")
    tabla_selecciones.heading("entrenador", text="Entrenador")
    tabla_selecciones.heading("jugadores", text="Jugadores")

    tabla_selecciones.pack(fill="both", expand=True, padx=10, pady=10)

    for seleccion in mundial.selecciones:
        tabla_selecciones.insert(
            "",
            tk.END,
            values=(
                seleccion.codigo_equipo,
                seleccion.pais.nombre,
                seleccion.entrenador.nombre + " " + seleccion.entrenador.apellido,
                len(seleccion.jugadores)
            )
        )

    def actualizar_pais():
        seleccionado = tabla_paises.selection()

        if seleccionado == ():
            messagebox.showerror("Error", "Seleccione un país de la tabla.")
            return

        valores = tabla_paises.item(seleccionado)["values"]
        codigo_actual = valores[0]

        pais_encontrado = None
        for pais in mundial.paises:
            if pais.codigo_fifa == codigo_actual:
                pais_encontrado = pais

        if pais_encontrado == None:
            messagebox.showerror("Error", "No se encontró el país.")
            return

        ventana_act = tk.Toplevel()
        ventana_act.title("Actualizar país")
        ventana_act.geometry("1920x1080")

        tk.Label(ventana_act, text="Código FIFA").pack()
        e_codigo = tk.Entry(ventana_act)
        e_codigo.pack()
        e_codigo.insert(0, pais_encontrado.codigo_fifa)

        tk.Label(ventana_act, text="Nombre").pack()
        e_nombre = tk.Entry(ventana_act)
        e_nombre.pack()
        e_nombre.insert(0, pais_encontrado.nombre)

        tk.Label(ventana_act, text="Continente").pack()
        e_continente = tk.Entry(ventana_act)
        e_continente.pack()
        e_continente.insert(0, pais_encontrado.continente)

        tk.Label(ventana_act, text="Ranking FIFA").pack()
        e_ranking = tk.Entry(ventana_act)
        e_ranking.pack()
        e_ranking.insert(0, pais_encontrado.ranking_fifa)

        def guardar_cambios():
            try:
                pais_encontrado.actualizar_datos(
                    e_codigo.get().upper(),
                    e_nombre.get(),
                    e_continente.get(),
                    int(e_ranking.get())
                )

                mundial.guardar_paises()
                mundial.guardar_selecciones()

                messagebox.showinfo("Éxito", "País actualizado correctamente.")
                ventana_act.destroy()
                ventana_lista.destroy()
                ver_paises_selecciones()

            except ValueError as error:
                messagebox.showerror("Error", str(error))

        tk.Button(ventana_act, text="Guardar cambios", command=guardar_cambios).pack(pady=15)

    def actualizar_seleccion():
        seleccionado = tabla_selecciones.selection()

        if seleccionado == ():
            messagebox.showerror("Error", "Seleccione una selección de la tabla.")
            return

        valores = tabla_selecciones.item(seleccionado)["values"]
        codigo_actual = valores[0]

        seleccion_encontrada = None
        for seleccion in mundial.selecciones:
            if seleccion.codigo_equipo == codigo_actual:
                seleccion_encontrada = seleccion

        if seleccion_encontrada == None:
            messagebox.showerror("Error", "No se encontró la selección.")
            return

        ventana_act = tk.Toplevel()
        ventana_act.title("Actualizar selección")
        ventana_act.geometry("1920x1080")

        tk.Label(ventana_act, text="Código de equipo").pack()
        e_codigo = tk.Entry(ventana_act)
        e_codigo.pack()
        e_codigo.insert(0, seleccion_encontrada.codigo_equipo)

        tk.Label(ventana_act, text="Licencia entrenador").pack()
        e_licencia = tk.Entry(ventana_act)
        e_licencia.pack()
        e_licencia.insert(0, seleccion_encontrada.entrenador.licencia)

        tk.Label(ventana_act, text="Experiencia entrenador").pack()
        e_experiencia = tk.Entry(ventana_act)
        e_experiencia.pack()
        e_experiencia.insert(0, seleccion_encontrada.entrenador.experiencia_años)

        tk.Label(ventana_act, text="Sistema de juego").pack()
        e_sistema = tk.Entry(ventana_act)
        e_sistema.pack()
        e_sistema.insert(0, seleccion_encontrada.entrenador.sistema_juego)

        def guardar_cambios():
            try:
                seleccion_encontrada.codigo_equipo = e_codigo.get()

                seleccion_encontrada.entrenador.actualizar_datos(
                    e_licencia.get(),
                    int(e_experiencia.get()),
                    e_sistema.get()
                )

                mundial.guardar_selecciones()

                messagebox.showinfo("Éxito", "Selección actualizada correctamente.")
                ventana_act.destroy()
                ventana_lista.destroy()
                ver_paises_selecciones()

            except ValueError as error:
                messagebox.showerror("Error", str(error))

        tk.Button(ventana_act, text="Guardar cambios", command=guardar_cambios).pack(pady=15)

    tk.Button(
        frame_paises,
        text="Actualizar país seleccionado",
        command=actualizar_pais
    ).pack(pady=5)

    tk.Button(
        frame_selecciones,
        text="Actualizar selección seleccionada",
        command=actualizar_seleccion
    ).pack(pady=5)

    boton_regresar(ventana_lista)

"""
    Descripción:
    Abre una ventana con un formulario para registrar un entrenador, solicitando sus datos personales y deportivos. Al guardar, crea un objeto Entrenador y lo agrega a la lista de entrenadores.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Agrega un entrenador a la lista de entrenadores.
    Restricciones:
    Los datos ingresados deben cumplir las validaciones de la clase Entrenador y la experiencia debe ser un número entero.
"""

def mostrar_Jugadores():

    ventanita = tk.Toplevel()
    ventanita.title("Entrenadores y Jugadores")
    ventanita.geometry("1920x1080")
    ventanita.configure(bg="#0f172a")

    tk.Label(
    ventanita,
    text="Administración de Entrenadores y Jugadores",
    font=("Arial", 20, "bold"),
    fg="pink",
    bg="#0f172a"
).pack(pady=20)
    
    tk.Button(
    ventanita,
    text="Registrar Entrenador",
    width=30,
    height=2,
    bg="#111827",
    fg="white",
    font=("Arial",11,"bold"),
    command=registrar_entrenador
).pack(pady=10)

    tk.Button(
    ventanita,
    text="Registrar Jugador",
    width=30,
    height=2,
    bg="#111827",
    fg="white",
    font=("Arial",11,"bold"),
    command=registrar_jugador
).pack(pady=10)
    
    tk.Button(
    ventanita,
    text="Ver Jugadores",
    width=30,
    height=2,
    bg="#111827",
    fg="white",
    font=("Arial",11,"bold"),
    command=ver_jugadores
).pack(pady=10)

    boton_regresar(ventanita)
    
"""
    Descripción:
    Abre una ventana con un formulario para registrar un entrenador, solicitando nombre, apellido, fecha de nacimiento, nacionalidad, licencia, experiencia y sistema de juego.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Crea un objeto Entrenador y lo agrega a la lista de entrenadores.
    Restricciones:
    Los datos ingresados deben cumplir las validaciones de la clase Entrenador y la experiencia debe ser un número entero.
"""

def registrar_entrenador():

    ventana_entrenador = tk.Toplevel()
    ventana_entrenador.title("Registrar Entrenador")
    ventana_entrenador.geometry("1920x1080")
    ventana_entrenador.configure(bg="#0f172a")

    tk.Label(ventana_entrenador, text="Nombre", bg="#0f172a", fg="white").pack()
    entry_nombre = tk.Entry(ventana_entrenador, width=30)
    entry_nombre.pack(pady=3)

    tk.Label(ventana_entrenador, text="Apellido", bg="#0f172a", fg="white").pack()
    entry_apellido = tk.Entry(ventana_entrenador, width=30)
    entry_apellido.pack(pady=3)

    tk.Label(ventana_entrenador, text="Fecha de nacimiento", bg="#0f172a", fg="white").pack()
    entry_fecha = tk.Entry(ventana_entrenador, width=30)
    entry_fecha.pack(pady=3)

    tk.Label(ventana_entrenador, text="Nacionalidad", bg="#0f172a", fg="white").pack()
    entry_nacionalidad = tk.Entry(ventana_entrenador, width=30)
    entry_nacionalidad.pack(pady=3)

    tk.Label(ventana_entrenador, text="Licencia", bg="#0f172a", fg="white").pack()
    entry_licencia = tk.Entry(ventana_entrenador, width=30)
    entry_licencia.pack(pady=3)

    tk.Label(ventana_entrenador, text="Experiencia", bg="#0f172a", fg="white").pack()
    entry_experiencia = tk.Entry(ventana_entrenador, width=30)
    entry_experiencia.pack(pady=3)

    tk.Label(ventana_entrenador, text="Sistema de juego", bg="#0f172a", fg="white").pack()
    entry_sistema = tk.Entry(ventana_entrenador, width=30)
    entry_sistema.pack(pady=3)

    def guardar():
        try:
            entrenador = Entrenador(
                entry_nombre.get(),
                entry_apellido.get(),
                entry_fecha.get(),
                entry_nacionalidad.get(),
                entry_licencia.get(),
                int(entry_experiencia.get()),
                entry_sistema.get()
            )

            lista_entrenadores.append(entrenador)

            messagebox.showinfo("Éxito", "Entrenador agregado correctamente.")
            ventana_entrenador.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventana_entrenador,
        text="Guardar",
        bg="#111827",
        fg="white",
        font=("Arial", 11, "bold"),
        width=20,
        command=guardar
    ).pack(pady=15)

    boton_regresar(ventana_entrenador)

"""
    Descripción:
    Abre una ventana con un formulario para registrar un jugador, solicitando sus datos personales, posición, dorsal, puntaje y la selección a la que pertenecerá. Al guardar, crea un objeto Futbolista, lo agrega a la selección correspondiente y actualiza el archivo de jugadores.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Agrega un jugador a la selección elegida y actualiza el archivo jugadores.txt.
    Restricciones:
    Debe existir al menos una selección registrada, el usuario debe seleccionar una selección válida y los datos ingresados deben cumplir las validaciones de la clase Futbolista.
"""
def registrar_jugador():

    ventana_jugador = tk.Toplevel()
    ventana_jugador.title("Registrar Jugador")
    ventana_jugador.geometry("1920x1080")
    ventana_jugador.configure(bg="#0f172a")
    
    tk.Label(ventana_jugador, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana_jugador)
    entry_nombre.pack()

    tk.Label(ventana_jugador, text="Apellido").pack()
    entry_apellido = tk.Entry(ventana_jugador)
    entry_apellido.pack()

    tk.Label(ventana_jugador, text="Fecha de nacimiento").pack()
    entry_fecha = tk.Entry(ventana_jugador)
    entry_fecha.pack()

    tk.Label(ventana_jugador, text="Nacionalidad").pack()
    entry_nacionalidad = tk.Entry(ventana_jugador)
    entry_nacionalidad.pack()

    tk.Label(ventana_jugador, text="Posición").pack()
    entry_posicion = tk.Entry(ventana_jugador)
    entry_posicion.pack()

    tk.Label(ventana_jugador, text="Dorsal").pack()
    entry_dorsal = tk.Entry(ventana_jugador)
    entry_dorsal.pack()

    tk.Label(ventana_jugador, text="Puntaje").pack()
    entry_puntaje = tk.Entry(ventana_jugador)
    entry_puntaje.pack()

    seleccion_var = tk.StringVar()

    opciones_seleccionadas = []

    for seleccion in mundial.selecciones:
        opciones_seleccionadas = opciones_seleccionadas + [seleccion.pais.nombre]

    if opciones_seleccionadas==[]:
        messagebox.showerror("Error", "no hay selecciones registradas")
        ventana_jugador.destroy()
        return
    seleccion_var = tk.StringVar()
    seleccion_var.set(opciones_seleccionadas[0])

    menu_selecciones = tk.OptionMenu(
        ventana_jugador,
        seleccion_var,
        *opciones_seleccionadas
    )
    menu_selecciones.pack()

    def guardar():

        try:
            jugador = Futbolista(
                entry_nombre.get(),
                entry_apellido.get(),
                entry_fecha.get(),
                entry_nacionalidad.get(),
                int(entry_dorsal.get()),
                entry_posicion.get(),
                int(entry_puntaje.get())
            )

            nombre_seleccion = seleccion_var.get()

            seleccion_encontrada = None

            for seleccion in mundial.selecciones:
                if seleccion.pais.nombre == nombre_seleccion:
                    seleccion_encontrada = seleccion

            if seleccion_encontrada == None:
                messagebox.showerror("Error", "Debe seleccionar una selección.")
                return

            seleccion_encontrada.agregar_jugador(jugador)

            mundial.guardar_jugadores()

            messagebox.showinfo(
                "Éxito",
                "Jugador agregado correctamente."
            )

            ventana_jugador.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
    ventana_jugador,
    text="Guardar",
    bg="#111827",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    command=guardar
).pack(pady=10)

    boton_regresar(ventana_jugador)

"""
    Descripción:
    Abre una ventana que muestra la lista de todos los jugadores registrados en las selecciones del Mundial, indicando su nombre, selección, posición, dorsal y puntaje.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Muestra en una lista la información de los jugadores registrados.
    Restricciones:
    Deben existir selecciones con jugadores registrados para que la lista muestre información.
"""
   
def ver_jugadores():
    
    ventanita = tk.Toplevel()
    ventanita.title("Jugadores registrados muy pros")
    ventanita.geometry("1920x1080")
    ventanita.configure(bg="#0f172a")

    tk.Label(
    ventanita,
    text="Jugadores Registrados",
    font=("Arial",20,"bold"),
    fg="pink",
    bg="#0f172a"
).pack(pady=10)

    frame_lista = tk.Frame(ventanita)
    frame_lista.pack(pady=10, fill="both", expand=True)

    scroll = tk.Scrollbar(frame_lista)
    scroll.pack(side="right", fill="y")

    lista = tk.Listbox(
        frame_lista,
        width=100,
        height=20,
        font=("Arial", 10),
        bg="#111827",
        fg="white",
        yscrollcommand=scroll.set
    )

    boton_regresar(ventanita)

    lista.pack(side="left", fill="both", expand=True)
    scroll.config(command=lista.yview)

    for seleccion in mundial.selecciones:

        for jugador in seleccion.jugadores:

            texto = (
                f"{jugador.nombre} "
                f"{jugador.apellido} | "
                f"Selección: {seleccion.pais.nombre} | "
                f"{jugador.posicion} | "
                f"Dorsal {jugador.dorsal} | "
                f"Puntaje {jugador.puntaje_individual}"
            )

            lista.insert(tk.END, texto)

"""
    Descripción:
    Abre una ventana para configurar el Mundial, permitiendo indicar la cantidad de grupos que se crearán. Verifica que existan suficientes selecciones registradas, crea los grupos de forma automática y muestra su composición en una lista.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Crea los grupos del Mundial y muestra las selecciones asignadas a cada uno.
    Restricciones:
    La cantidad de grupos debe ser mayor o igual a 2 y deben existir exactamente cuatro selecciones por cada grupo que se desea crear.
"""

def abrirMundial():

    ventanita = tk.Toplevel()
    ventanita.title("Configurar Mundial")
    ventanita.geometry("1920x1080")
    ventanita.configure(bg="#0f172a")

    tk.Label(
        ventanita,
        text="Configurar mundial uwu",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=15)

    tk.Label(
        ventanita,
        text="Cantidad de grupos a crear:",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack()

    entry_grupos = tk.Entry(ventanita, width=20)
    entry_grupos.pack(pady=5)

    frame_lista = tk.Frame(
        ventanita,
        bg="#0f172a"
    )
    frame_lista.pack(pady=15)

    scroll = tk.Scrollbar(frame_lista)
    scroll.pack(side="right", fill="y")

    lista = tk.Listbox(
        frame_lista,
        width=80,
        height=18,
        bg="#111827",
        fg="white",
        font=("Arial", 10),
        yscrollcommand=scroll.set
    )
    lista.pack(side="left", fill="both")

    scroll.config(command=lista.yview)

    def crear_grupos():
        try:
            cantidad_grupos = int(entry_grupos.get())

            if cantidad_grupos < 2:
                messagebox.showerror(
                    "Error",
                    "La cantidad de grupos debe ser mínimo 2."
                )
                return

            selecciones_necesarias = cantidad_grupos * 4

            if len(mundial.selecciones) != selecciones_necesarias:
                messagebox.showerror(
                    "Error",
                    "Para crear " + str(cantidad_grupos) +
                    " grupos se necesitan exactamente " +
                    str(selecciones_necesarias) +
                    " selecciones registradas.\n\nActualmente hay " +
                    str(len(mundial.selecciones)) + "."
                )
                return

            mundial.crear_grupos(cantidad_grupos)

            lista.delete(0, tk.END)

            lista.insert(tk.END, "GRUPOS FORMADOS:")
            lista.insert(tk.END, "")

            for grupo in mundial.grupos:
                lista.insert(tk.END, grupo.nombre_grupo)

                for equipo in grupo.equipos:
                    lista.insert(
                        tk.END,
                        "   - " + equipo.pais.nombre +
                        " (" + equipo.codigo_equipo + ")"
                    )

                lista.insert(tk.END, "")

            messagebox.showinfo(
                "Éxito",
                "Grupos creados correctamente."
            )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventanita,
        text="Crear grupos",
        font=("Arial", 12, "bold"),
        bg="#111111",
        fg="white",
        width=25,
        command=crear_grupos
    ).pack(pady=5)

    tk.Button(
        ventanita,
        text="Regresar",
        font=("Arial", 11, "bold"),
        bg="#7f1d1d",
        fg="white",
        width=20,
        command=ventanita.destroy
    ).pack(pady=10)

"""
    Descripción:
    Abre una ventana para simular el Mundial FIFA 2026, permitiendo jugar la fase de grupos, mostrar resultados y tablas de posiciones, avanzar por las fases eliminatorias y determinar la selección campeona.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Muestra en pantalla los resultados de partidos, clasificados, fases eliminatorias y campeón del Mundial.
    Restricciones:
    Los grupos deben estar configurados previamente, las selecciones deben tener jugadores registrados y se debe simular la fase de grupos antes de avanzar a las fases eliminatorias.
"""

def jugarMundial():

    ventanita = tk.Toplevel()
    ventanita.title("Jugar Mundial")
    ventanita.geometry("1920x1080")
    ventanita.configure(bg="#0f172a")

    tk.Label(
        ventanita,
        text="JUGAR MUNDIAL FIFA 2026",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=10)

    frame_lista = tk.Frame(ventanita, bg="#0f172a")
    frame_lista.pack(pady=10)

    scroll = tk.Scrollbar(frame_lista)
    scroll.pack(side="right", fill="y")

    lista = tk.Listbox(
        frame_lista,
        width=120,
        height=25,
        bg="#111827",
        fg="white",
        font=("Arial", 10),
        yscrollcommand=scroll.set
    )
    lista.pack(side="left", fill="both")

    scroll.config(command=lista.yview)

    estado = {
        "clasificados": [],
        "fase_grupos_jugada": False
    }

    def nombre_fase(cantidad):
        if cantidad == 32:
            return "Dieciseisavos de final"
        elif cantidad == 16:
            return "Octavos de final"
        elif cantidad == 8:
            return "Cuartos de final"
        elif cantidad == 4:
            return "Semifinales"
        elif cantidad == 2:
            return "Final"
        else:
            return "Fase con " + str(cantidad) + " equipos"

    def simular_grupos():
        try:
            if len(mundial.grupos) == 0:
                messagebox.showerror(
                    "Error",
                    "Primero debe configurar los grupos."
                )
                return

            for seleccion in mundial.selecciones:
                if len(seleccion.jugadores) == 0:
                    messagebox.showerror(
                        "Error",
                        "La selección " + seleccion.pais.nombre +
                        " no tiene jugadores registrados."
                    )
                    return

                seleccion.calcular_fuerza_equipo()

            mundial.jugar_fase_grupos()

            lista.delete(0, tk.END)
            lista.insert(tk.END, "RESULTADOS DE LA FASE DE GRUPOS")
            lista.insert(tk.END, "")

            clasificados = []

            for grupo in mundial.grupos:
                lista.insert(tk.END, grupo.nombre_grupo)
                lista.insert(tk.END, "Partidos:")

                for partido in grupo.partidos:
                    texto = (
                        partido.equipo1.pais.nombre + " " +
                        str(partido.goles_equipo1) + " - " +
                        str(partido.goles_equipo2) + " " +
                        partido.equipo2.pais.nombre
                    )
                    lista.insert(tk.END, "   " + texto)

                lista.insert(tk.END, "")
                lista.insert(tk.END, "Tabla final:")

                tabla = grupo.calcular_tabla()

                for info in tabla:
                    equipo = info[0]
                    puntos = info[1]
                    goles_favor = info[2]
                    goles_contra = info[3]
                    diferencia = goles_favor - goles_contra

                    texto_tabla = (
                        "   " + equipo.pais.nombre +
                        " | Pts: " + str(puntos) +
                        " | GF: " + str(goles_favor) +
                        " | GC: " + str(goles_contra) +
                        " | Dif: " + str(diferencia)
                    )

                    lista.insert(tk.END, texto_tabla)

                primer_lugar, segundo_lugar = grupo.obtener_clasificados()
                clasificados = clasificados + [primer_lugar, segundo_lugar]

                lista.insert(tk.END, "")
                lista.insert(
                    tk.END,
                    "Clasificados: " +
                    primer_lugar.pais.nombre + " y " +
                    segundo_lugar.pais.nombre
                )
                lista.insert(tk.END, "________________________________")
                lista.insert(tk.END, "")

            estado["clasificados"] = clasificados
            estado["fase_grupos_jugada"] = True

            messagebox.showinfo(
                "Éxito",
                "Fase de grupos simulada correctamente."
            )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def avanzar_fase():
        try:
            if estado["fase_grupos_jugada"] == False:
                messagebox.showerror(
                    "Error",
                    "Primero debe simular la fase de grupos."
                )
                return

            if len(estado["clasificados"]) <= 1:
                messagebox.showinfo(
                    "Mundial finalizado",
                    "El mundial ya finalizó."
                )
                return

            cantidad = len(estado["clasificados"])
            fase_nombre = nombre_fase(cantidad)

            fase = mundial.armar_fase_eliminatoria(
                fase_nombre,
                estado["clasificados"]
            )

            nuevos_clasificados = mundial.jugar_fase_eliminatoria(fase)

            lista.insert(tk.END, "")
            lista.insert(tk.END, "_________________________________________")
            lista.insert(tk.END, fase_nombre.upper())
            lista.insert(tk.END, "_________________________________________")

            for partido in fase.partidos:
                texto = (
                    partido.equipo1.pais.nombre + " " +
                    str(partido.goles_equipo1) + " - " +
                    str(partido.goles_equipo2) + " " +
                    partido.equipo2.pais.nombre
                )

                if partido.gano_por_penales:
                    texto = (
                        texto +
                        " | Penales: " +
                        str(partido.penales_equipo1) + " - " +
                        str(partido.penales_equipo2)
                    )

                ganador = partido.generar_ganador()

                lista.insert(tk.END, texto)
                lista.insert(tk.END, "   Ganador: " + ganador.pais.nombre)
                lista.insert(tk.END, "")

            estado["clasificados"] = nuevos_clasificados

            if len(nuevos_clasificados) == 1:
                mundial.campeon = nuevos_clasificados[0]

                lista.insert(tk.END, "")
                lista.insert(tk.END, "CAMPEÓN DEL MUNDIAL FIFA 2026")
                lista.insert(tk.END, mundial.campeon.pais.nombre.upper())

                messagebox.showinfo(
                    "CAMPEÓN DEL MUNDIAL",
                    "La selección campeona es: " +
                    mundial.campeon.pais.nombre
                )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    tk.Button(
        ventanita,
        text="Simular fase de grupos",
        font=("Arial", 12, "bold"),
        bg="#111111",
        fg="white",
        width=30,
        command=simular_grupos
    ).pack(pady=5)

    tk.Button(
        ventanita,
        text="Avanzar a siguiente fase",
        font=("Arial", 12, "bold"),
        bg="#1E88E5",
        fg="white",
        width=30,
        command=avanzar_fase
    ).pack(pady=5)

    tk.Button(
        ventanita,
        text="Regresar",
        font=("Arial", 11, "bold"),
        bg="#7f1d1d",
        fg="white",
        width=20,
        command=ventanita.destroy
    ).pack(pady=5)

"""
    Descripción:
    Abre una ventana para mostrar las estadísticas y rankings del Mundial, incluyendo tabla de goleadores, desempeño de selecciones, selección con más goles, selección con más tarjetas y campeón del torneo.
    Entradas:
    Ninguna.
    Salidas:
    No retorna ningún valor. Muestra tablas y un resumen con las estadísticas del Mundial.
    Restricciones:
    Para mostrar estadísticas completas, el Mundial debe haber sido jugado previamente y deben existir selecciones, jugadores, partidos y fases registradas.
"""

def verEstadisticas():

    ventanita = tk.Toplevel()
    ventanita.title("Estadísticas y Rankings")
    ventanita.geometry("1920x1080")
    ventanita.configure(bg="#0f172a")

    tk.Label(
        ventanita,
        text="ESTADÍSTICAS Y RANKINGS",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=10)

    notebook = ttk.Notebook(ventanita)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    frame_goleadores = tk.Frame(notebook, bg="#0f172a")
    frame_selecciones = tk.Frame(notebook, bg="#0f172a")
    frame_resumen = tk.Frame(notebook, bg="#0f172a")

    notebook.add(frame_goleadores, text="Goleadores")
    notebook.add(frame_selecciones, text="Selecciones")
    notebook.add(frame_resumen, text="Resumen")

    tabla_goleadores = ttk.Treeview(
        frame_goleadores,
        columns=("jugador", "seleccion", "goles"),
        show="headings"
    )

    tabla_goleadores.heading("jugador", text="Jugador")
    tabla_goleadores.heading("seleccion", text="Selección")
    tabla_goleadores.heading("goles", text="Goles")

    tabla_goleadores.pack(fill="both", expand=True, padx=10, pady=10)

    jugadores = []

    for seleccion in mundial.selecciones:
        for jugador in seleccion.jugadores:
            jugadores = jugadores + [(jugador, seleccion)]

    n = len(jugadores)
    for i in range(n):
        for j in range(n - 1 - i):
            if jugadores[j][0].goles < jugadores[j + 1][0].goles:
                temporal = jugadores[j]
                jugadores[j] = jugadores[j + 1]
                jugadores[j + 1] = temporal

    for dato in jugadores:
        jugador = dato[0]
        seleccion = dato[1]

        tabla_goleadores.insert(
            "",
            tk.END,
            values=(
                jugador.nombre + " " + jugador.apellido,
                seleccion.pais.nombre,
                jugador.goles
            )
        )

    tabla_selecciones = ttk.Treeview(
        frame_selecciones,
        columns=("seleccion", "puntos", "gf", "gc", "dif", "fase"),
        show="headings"
    )

    tabla_selecciones.heading("seleccion", text="Selección")
    tabla_selecciones.heading("puntos", text="Puntos")
    tabla_selecciones.heading("gf", text="Goles favor")
    tabla_selecciones.heading("gc", text="Goles contra")
    tabla_selecciones.heading("dif", text="Diferencia")
    tabla_selecciones.heading("fase", text="Fase alcanzada")

    tabla_selecciones.pack(fill="both", expand=True, padx=10, pady=10)

    datos_selecciones = []

    for seleccion in mundial.selecciones:

        puntos = 0

        for grupo in mundial.grupos:
            for partido in grupo.partidos:

                if partido.equipo1 == seleccion:
                    if partido.goles_equipo1 > partido.goles_equipo2:
                        puntos += 3
                    elif partido.goles_equipo1 == partido.goles_equipo2:
                        puntos += 1

                elif partido.equipo2 == seleccion:
                    if partido.goles_equipo2 > partido.goles_equipo1:
                        puntos += 3
                    elif partido.goles_equipo2 == partido.goles_equipo1:
                        puntos += 1

        diferencia = seleccion.total_goles_favor - seleccion.total_goles_contra

        fase_alcanzada = "Fase de grupos"

        for fase in mundial.fases:
            for partido in fase.partidos:
                if partido.equipo1 == seleccion or partido.equipo2 == seleccion:
                    fase_alcanzada = fase.nombre_fase

        if mundial.campeon == seleccion:
            fase_alcanzada = "Campeón"

        datos_selecciones = datos_selecciones + [
            (
                seleccion,
                puntos,
                seleccion.total_goles_favor,
                seleccion.total_goles_contra,
                diferencia,
                fase_alcanzada
            )
        ]

    n = len(datos_selecciones)
    for i in range(n):
        for j in range(n - 1 - i):
            actual = datos_selecciones[j]
            siguiente = datos_selecciones[j + 1]

            if actual[1] < siguiente[1]:
                temporal = datos_selecciones[j]
                datos_selecciones[j] = datos_selecciones[j + 1]
                datos_selecciones[j + 1] = temporal
            elif actual[1] == siguiente[1]:
                if actual[4] < siguiente[4]:
                    temporal = datos_selecciones[j]
                    datos_selecciones[j] = datos_selecciones[j + 1]
                    datos_selecciones[j + 1] = temporal

    for dato in datos_selecciones:
        seleccion = dato[0]

        tabla_selecciones.insert(
            "",
            tk.END,
            values=(
                seleccion.pais.nombre,
                dato[1],
                dato[2],
                dato[3],
                dato[4],
                dato[5]
            )
        )

    mas_goles = None
    mas_tarjetas = None

    for seleccion in mundial.selecciones:

        if mas_goles == None:
            mas_goles = seleccion
        elif seleccion.total_goles_favor > mas_goles.total_goles_favor:
            mas_goles = seleccion

        tarjetas_seleccion = (
            seleccion.total_tarjetas_amarillas +
            seleccion.total_tarjetas_rojas
        )

        if mas_tarjetas == None:
            mas_tarjetas = seleccion
        else:
            tarjetas_mayor = (
                mas_tarjetas.total_tarjetas_amarillas +
                mas_tarjetas.total_tarjetas_rojas
            )

            if tarjetas_seleccion > tarjetas_mayor:
                mas_tarjetas = seleccion

    texto_resumen = ""

    if mas_goles != None:
        texto_resumen += (
            "Selección con más goles anotados:\n" +
            mas_goles.pais.nombre +
            " | Goles: " +
            str(mas_goles.total_goles_favor) +
            "\n\n"
        )

    if mas_tarjetas != None:
        texto_resumen += (
            "Selección con más tarjetas:\n" +
            mas_tarjetas.pais.nombre +
            " | Amarillas: " +
            str(mas_tarjetas.total_tarjetas_amarillas) +
            " | Rojas: " +
            str(mas_tarjetas.total_tarjetas_rojas) +
            "\n\n"
        )

    if mundial.campeon != None:
        texto_resumen += (
            "Campeón del Mundial FIFA 2026:\n" +
            mundial.campeon.pais.nombre
        )

    if texto_resumen == "":
        texto_resumen = "Aún no hay estadísticas. Primero debe jugar el mundial. entonces victor le dice a joel.. montate en mi motoaora >:) pero entonces joel le dice a victor... DESAYUNA CON HUEVO !! pero victor le dice a joel.. feliz navidad y prospero año nuevo:"

    tk.Label(
        frame_resumen,
        text=texto_resumen,
        font=("Arial", 15, "bold"),
        fg="white",
        bg="#0f172a",
        justify="left"
    ).pack(pady=40)

    boton_regresar(ventanita)

"""
    Descripción:
    Cambia el color de fondo del botón cuando el cursor del mouse entra sobre él.
    Entradas:
    event: Evento generado al pasar el cursor sobre un botón.
    Salidas:
    No retorna ningún valor. Modifica el color del botón.
    Restricciones:
    El evento debe provenir de un widget tipo Button.
"""

def entrar(event):
    event.widget.config(bg="#1E88E5")

"""
    Descripción:
    Restaura el color original del botón cuando el cursor del mouse sale de él.
    Entradas:
    event: Evento generado al retirar el cursor de un botón.
    Salidas:
    No retorna ningún valor. Restaura el color del botón.
    Restricciones:
    El evento debe provenir de un widget tipo Button.
"""

def salir(event):
    event.widget.config(bg="#111111")


frame_botones = tk.Frame(
    ventana,
    bg="#000000"
)
frame_botones.pack(pady=70)


btn_paises = tk.Button(
    frame_botones,
    text="Administrar Países y Selecciones",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111",
    activebackground="#1E88E5",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=32,
    height=2,
    cursor="hand2",
    command=openPaises
)
btn_paises.pack(pady=8)


btn_entrenadores = tk.Button(
    frame_botones,
    text="Entrenadores y Jugadores",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111",
    activebackground="#1E88E5",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=32,
    height=2,
    cursor="hand2",
    command=mostrar_Jugadores
)
btn_entrenadores.pack(pady=8)


btn_configuracion = tk.Button(
    frame_botones,
    text="Configurar Mundial",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111",
    activebackground="#1E88E5",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=32,
    height=2,
    cursor="hand2",
    command=abrirMundial
)
btn_configuracion.pack(pady=8)


btn_jugar = tk.Button(
    frame_botones,
    text="Jugar Mundial",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111",
    activebackground="#1E88E5",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=32,
    height=2,
    cursor="hand2",
    command=jugarMundial
)
btn_jugar.pack(pady=8)


btn_estadisticas = tk.Button(
    frame_botones,
    text="Estadísticas y Rankings",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#111111",
    activebackground="#1E88E5",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=32,
    height=2,
    cursor="hand2",
    command=verEstadisticas
)
btn_estadisticas.pack(pady=8)


for boton in [
    btn_paises,
    btn_entrenadores,
    btn_configuracion,
    btn_jugar,
    btn_estadisticas
]:
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)


ventana.mainloop()
