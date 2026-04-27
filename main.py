class ErrorDatosInvalidos(Exception):
    pass

class DeportistaNoEncontrado(Exception):
    pass

class DeporteIncorrecto(Exception):
    pass

class DeportistaYaInscrito(Exception):
    pass

class DeportistaNoInscrito(Exception):
    pass

class Deportista:

    @property
    def puntaje(self):
        return self.__puntaje

    @property
    def cantidad_de_competencias(self):
        return self.__cantidad_de_competencias

    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias):

        if not nombre:
            raise ErrorDatosInvalidos("El nombre no puede estar vacío.")

        if edad <= 0:
            raise ErrorDatosInvalidos("La edad debe ser mayor a 0.")

        if puntaje < 0:
            raise ErrorDatosInvalidos("El puntaje no puede ser negativo.")

        if cantidad_de_competencias < 0:
            raise ErrorDatosInvalidos("La cantidad de competencias no puede ser negativa.")
    
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.__puntaje = puntaje
        self.__cantidad_de_competencias = cantidad_de_competencias

    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDeporte: {self.deporte}\nPuntaje: {self.__puntaje}\nCantidad de Competencias: {self.__cantidad_de_competencias}"

    def obtener_informacion_basica(self):
        print(f"{self.nombre} realiza: {self.deporte}")

    def obtener_estadisticas(self):
        print(f"El deportista {self.nombre} tiene:")
        print(f"Puntaje -> {self.__puntaje}")
        print(f"Cantidad de competencias -> {self.__cantidad_de_competencias}\n")

    def reiniciar_puntaje(self):
        self.__cantidad_de_competencias = 0
        self.__puntaje = 0
    
    def actualizar_puntaje_y_competencias(self, nuevo_puntaje):
        if nuevo_puntaje < 0:
            raise ErrorDatosInvalidos("El nuevo puntaje no puede ser negativo.")
        
        self.__puntaje += nuevo_puntaje
        self.__cantidad_de_competencias += 1 

class Registro:
    def __init__(self):
        self.deportistas = []

    def añadir_deportista(self, deportista):
        for dep in self.deportistas:
            if (dep == deportista):
                raise ErrorDatosInvalidos("Deportista ya estaba registrado, por ende no se ingresó.")
        self.deportistas.append(deportista)
    
    def mostrar_deportistas(self):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            print(f"{i}.- {dep.nombre} -> {dep.puntaje}")
            i += 1

    def mostrar_ranking_por_deporte(self, deporte):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            if (dep.deporte == deporte):
                print(f"{i}.- {dep.nombre} -> {dep.puntaje}")
                i += 1
    
    def mostrar_n_mejores_deportistas(self, deporte, n):
        if (n <= 0):
            raise ErrorDatosInvalidos("La cantidad de deportistas a mostrar debe ser mayor a 0.")
        
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            if (dep.deporte == deporte and i <= n):
                print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
                i += 1

    def buscar_deportista(self, nombre):
        for dep in self.deportistas:
            if (dep.nombre == nombre):
                return dep
        raise DeportistaNoEncontrado(f"Deportista '{nombre}' no encontrado en el registro.")

class Competencia:
    def __init__(self, nombre, fecha, participantes, resultados, deporte, registro):

        if not nombre:
            raise ErrorDatosInvalidos("El nombre de la competencia no puede estar vacío.")

        if not fecha:
            raise ErrorDatosInvalidos("La fecha de la competencia no puede estar vacía.")

        if not deporte:
            raise ErrorDatosInvalidos("El deporte de la competencia no puede estar vacío.")
        
        self.nombre = nombre
        self.fecha = fecha
        self.participantes = participantes
        self.resultados = resultados
        self.deporte = deporte
        self.registro = registro
    
    def inscribir_participante(self, deportista):
        deportista_registrado = self.registro.buscar_deportista(deportista.nombre)

        if deportista_registrado.deporte != self.deporte:
            raise DeporteIncorrecto(
                f"{deportista_registrado.nombre} practica {deportista_registrado.deporte}, no {self.deporte}."
            )

        if deportista_registrado in self.participantes:
            raise DeportistaYaInscrito(
                f"{deportista_registrado.nombre} ya está inscrito en la competencia."
            )

        self.participantes.append(deportista_registrado)
        print(f"{deportista_registrado.nombre} fue inscrito correctamente.")


    def registrar_resultado(self, resultado):
        if not isinstance(resultado, dict):
            raise ErrorDatosInvalidos("El resultado debe entregarse como un diccionario.")

        if not resultado:
            raise ErrorDatosInvalidos("El resultado no puede estar vacío.")

        for nombre_deportista, puntaje_obtenido in resultado.items():

            if not nombre_deportista:
                raise ErrorDatosInvalidos("El nombre del deportista no puede estar vacío.")

            if not isinstance(puntaje_obtenido, (int, float)):
                raise ErrorDatosInvalidos(
                    f"El puntaje de {nombre_deportista} debe ser un número."
                )

            if puntaje_obtenido < 0:
                raise ErrorDatosInvalidos(
                    f"El puntaje de {nombre_deportista} no puede ser negativo."
                )

            encontrado = None

            for deportista in self.participantes:
                if deportista.nombre == nombre_deportista:
                    encontrado = deportista
                    break

            if encontrado is None:
                raise DeportistaNoInscrito(
                    f"{nombre_deportista} no está inscrito en la competencia."
                )

            self.resultados[nombre_deportista] = puntaje_obtenido
            encontrado.actualizar_puntaje_y_competencias(puntaje_obtenido)

        print("Resultados registrados correctamente.\n")
    
    def mostrar_resultado(self):
        if not self.resultados:
            raise ErrorDatosInvalidos(
                "No hay resultados registrados para esta competencia."
            )

        print(f"Resultados de la competencia: {self.nombre}")

        resultados_ordenados = sorted(
            self.resultados.items(),
            key=lambda item: item[1],
            reverse=True
        )

        i = 1
        for nombre, puntaje in resultados_ordenados:
            print(f"{i}.- {nombre} -> {puntaje}")
            i += 1

        print()
    
    def mostrar_n_posiciones(self, n):
        if n <= 0:
            raise ErrorDatosInvalidos("El número de posiciones debe ser mayor a 0.")

        self.participantes.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for deportista in self.participantes:
            if (i <= n):
                print(f"{i}.- {deportista.nombre} -> {deportista.puntaje}")
                i += 1
            else: return

class Futbolista(Deportista):
    def __init__(self, nombre, edad, puntaje, cantidad_de_competencias, equipo, goles, asistencias, posicion):
        super().__init__(nombre, edad, "Futbol", puntaje, cantidad_de_competencias)

        if not equipo:
            raise ErrorDatosInvalidos("El equipo no puede estar vacío.")

        if goles < 0:
            raise ErrorDatosInvalidos("Los goles no pueden ser negativos.")

        if asistencias < 0:
            raise ErrorDatosInvalidos("Las asistencias no pueden ser negativas.")

        if not posicion:
            raise ErrorDatosInvalidos("La posición no puede estar vacía.")

        self.equipo = equipo
        self.goles = goles
        self.asistencias = asistencias
        self.posicion = posicion

    def obtener_informacion_basica(self):
        super().obtener_informacion_basica()
        print(f"Posición: {self.posicion}")
        print(f"Puntaje: {self.puntaje}")

    def añadir_goles(self, goles):
        if goles <= 0:
            raise ErrorDatosInvalidos("El valor de goles a ingresar debe ser mayor a 0.")
        self.goles += goles

    def añadir_asistencias(self, asistencias):
        if asistencias <= 0:
            raise ErrorDatosInvalidos("El valor de asistencias a ingresar debe ser mayor a 0.")
        self.asistencias += asistencias

    def calcular_rendimiento(self):
        if self.cantidad_de_competencias == 0:
            raise ErrorDatosInvalidos("No se puede calcular rendimiento sin competencias registradas.")

        rendimiento = (self.goles*2 + self.asistencias*0.7)/self.cantidad_de_competencias
        print(f"El rendimiento de {self.nombre} es de {rendimiento}")
        return rendimiento

    def cambiar_de_equipo(self, nuevo_equipo):
        self.equipo = nuevo_equipo
        self.reiniciar_puntaje()

class Tenista(Deportista):
    def __init__(self, nombre, edad, puntaje, cantidad_de_competencias, pareja, ranking_atp):
        super().__init__(nombre, edad, "Tenis", puntaje, cantidad_de_competencias)

        if ranking_atp <= 0:
            raise ErrorDatosInvalidos("El ranking ATP debe ser mayor a 0.")

        self.pareja = pareja
        self.ranking_atp = ranking_atp

    def obtener_informacion_basica(self):
        super().obtener_informacion_basica()
        print(f"Ranking ATP: {self.ranking_atp}")
        print(f"Puntaje: {self.puntaje}")
    
    def actualizar_de_pareja(self, nueva_pareja):
        self.reiniciar_puntaje()
        self.pareja = nueva_pareja

class Atleta(Deportista):
    def __init__(self, nombre, edad, puntaje, cantidad_de_competencias, disciplina):
        super().__init__(nombre, edad, "Atletismo", puntaje, cantidad_de_competencias)

        if not disciplina:
            raise ErrorDatosInvalidos("La disciplina no puede estar vacía.")

        self.disciplina = disciplina
        self.mejores_tiempos = []

    def obtener_informacion_basica(self):
        super().obtener_informacion_basica()
        print(f"Disciplina: {self.disciplina}")
        print(f"Mejores tiempos: {self.mejores_tiempos}")

    def agregar_mejores_tiempos(self, tiempo):
        if tiempo <= 0:
            raise ErrorDatosInvalidos("El tiempo debe ser mayor a 0.")

        self.mejores_tiempos.append(tiempo)

"""
============================================================
Script que simula el ingreso de deportistas y competencias.
============================================================
"""

if __name__ == "__main__":

    print("======================================")
    print(" SISTEMA DE DEPORTISTAS Y COMPETENCIAS")
    print("======================================\n")

    try:
        # Crear registro
        registro = Registro()

        # Crear deportistas
        futbolista1 = Futbolista(
            nombre="Carlos",
            edad=22,
            puntaje=100,
            cantidad_de_competencias=5,
            equipo="Colo Colo",
            goles=12,
            asistencias=4,
            posicion="Delantero"
        )

        futbolista2 = Futbolista(
            nombre="Pedro",
            edad=24,
            puntaje=85,
            cantidad_de_competencias=4,
            equipo="Universidad de Chile",
            goles=8,
            asistencias=6,
            posicion="Mediocampista"
        )

        futbolista3 = Futbolista(
            nombre="Matias",
            edad=20,
            puntaje=70,
            cantidad_de_competencias=3,
            equipo="Magallanes",
            goles=5,
            asistencias=3,
            posicion="Defensa"
        )

        tenista1 = Tenista(
            nombre="Ana",
            edad=21,
            puntaje=95,
            cantidad_de_competencias=6,
            pareja="Sin pareja",
            ranking_atp=120
        )

        tenista2 = Tenista(
            nombre="Rodrigo",
            edad=21,
            puntaje=0,
            cantidad_de_competencias=0,
            pareja="Sin pareja",
            ranking_atp=10000
        )

        atleta1 = Atleta(
            nombre="Luis",
            edad=19,
            puntaje=75,
            cantidad_de_competencias=3,
            disciplina="100 metros planos"
        )

        # Agregar deportistas al registro
        registro.añadir_deportista(futbolista1)
        registro.añadir_deportista(futbolista2)
        registro.añadir_deportista(futbolista3)
        registro.añadir_deportista(tenista1)
        registro.añadir_deportista(atleta1)

        print("=== DEPORTISTAS REGISTRADOS ===")
        registro.mostrar_deportistas()
        print()

        print("=== INFORMACIÓN BÁSICA DE DEPORTISTAS ===")
        futbolista1.obtener_informacion_basica()
        print()

        tenista1.obtener_informacion_basica()
        print()

        atleta1.obtener_informacion_basica()
        print()

        print("=== ESTADÍSTICAS DE UN DEPORTISTA ===")
        futbolista1.obtener_estadisticas()

        print("=== RANKING POR DEPORTE: FUTBOL ===")
        registro.mostrar_ranking_por_deporte("Futbol")
        print()

        print("=== 2 MEJORES FUTBOLISTAS ===")
        registro.mostrar_n_mejores_deportistas("Futbol", 2)
        print()

        print("=== BÚSQUEDA DE DEPORTISTA ===")
        deportista_buscado = registro.buscar_deportista("Ana")
        print(deportista_buscado)
        print()

        print("=== RENDIMIENTO FUTBOLISTA ===")
        futbolista1.calcular_rendimiento()
        print()

        # Métodos de Futbolista
        print("=== ACTUALIZANDO DATOS DE FUTBOLISTA ===")
        futbolista1.añadir_goles(2)
        futbolista1.añadir_asistencias(1)
        futbolista1.calcular_rendimiento()
        print()

        # Método de Tenista
        print("=== ACTUALIZANDO PAREJA DE TENISTA ===")
        tenista1.actualizar_de_pareja("María")
        tenista1.obtener_informacion_basica()
        print()

        # Método de Atleta
        print("=== AGREGANDO TIEMPOS DE ATLETA ===")
        atleta1.agregar_mejores_tiempos(11.25)
        atleta1.agregar_mejores_tiempos(10.98)
        atleta1.obtener_informacion_basica()
        print()

        # Crear competencia de fútbol
        competencia_futbol = Competencia(
            nombre="Copa Regional de Fútbol",
            fecha="2026-04-26",
            participantes=[],
            resultados={},
            deporte="Futbol",
            registro=registro
        )

        print("=== INSCRIPCIÓN DE PARTICIPANTES EN FÚTBOL ===")
        competencia_futbol.inscribir_participante(futbolista1)
        competencia_futbol.inscribir_participante(futbolista2)
        competencia_futbol.inscribir_participante(futbolista3)
        print()

        print("=== REGISTRO DE RESULTADOS DE FÚTBOL ===")

        resultado_futbol = {
            "Carlos": 30,
            "Pedro": 25,
            "Matias": 18
        }

        competencia_futbol.registrar_resultado(resultado_futbol)

        print("=== RESULTADOS DE LA COMPETENCIA DE FÚTBOL ===")
        competencia_futbol.mostrar_resultado()

        print("=== PODIO DE LA COMPETENCIA DE FÚTBOL ===")
        competencia_futbol.mostrar_n_posiciones(3)
        print()

        print("=== RANKING GENERAL ACTUALIZADO ===")
        registro.mostrar_deportistas()
        print()

        # Crear competencia de tenis
        competencia_tenis = Competencia(
            nombre="Torneo Regional de Tenis",
            fecha="2026-05-10",
            participantes=[],
            resultados={},
            deporte="Tenis",
            registro=registro
        )

        print("=== INSCRIPCIÓN DE PARTICIPANTES EN TENIS ===")
        competencia_tenis.inscribir_participante(tenista1)
        print()

        print("=== REGISTRO DE RESULTADOS DE TENIS ===")

        resultado_tenis = {
            "Ana": 40
        }

        competencia_tenis.registrar_resultado(resultado_tenis)

        print("=== RESULTADOS DE LA COMPETENCIA DE TENIS ===")
        competencia_tenis.mostrar_resultado()

        print("=== PRUEBAS DE ERRORES CONTROLADOS ===")

        # Error 1: intentar inscribir a una tenista en fútbol
        try:
            competencia_futbol.inscribir_participante(tenista1)
        except DeporteIncorrecto as e:
            print(f"Error controlado: {e}")

        # Error 2: intentar inscribir a alguien que no existe
        try:
            competencia_futbol.inscribir_participante(tenista2)
        except DeportistaNoEncontrado as e:
            print(f"Error controlado: {e}")

        # Error 3: intentar registrar resultado de alguien no inscrito
        try:
            competencia_futbol.registrar_resultado({"Ana": 50})
        except DeportistaNoInscrito as e:
            print(f"Error controlado: {e}")

        # Error 4: intentar registrar puntaje negativo
        try:
            competencia_futbol.registrar_resultado({"Carlos": -10})
        except ErrorDatosInvalidos as e:
            print(f"Error controlado: {e}")

        # Error 5: intentar mostrar resultados de una competencia sin resultados
        try:
            competencia_atletismo = Competencia(
                nombre="Torneo de Atletismo",
                fecha="2026-06-01",
                participantes=[],
                resultados={},
                deporte="Atletismo",
                registro=registro
            )

            competencia_atletismo.inscribir_participante(atleta1)
            competencia_atletismo.mostrar_resultado()

        except ErrorDatosInvalidos as e:
            print(f"Error controlado: {e}")

    except ErrorDatosInvalidos as e:
        print(f"Error de datos: {e}")

    except DeportistaNoEncontrado as e:
        print(f"Error de búsqueda: {e}")

    except DeporteIncorrecto as e:
        print(f"Error de deporte: {e}")

    except DeportistaYaInscrito as e:
        print(f"Error de inscripción: {e}")

    except DeportistaNoInscrito as e:
        print(f"Error de resultado: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")