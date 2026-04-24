class ErrorDatosInvalidos(Exception):
    pass


class DeportistaNoEncontrado(Exception):
    pass


class DeporteIncorrecto(Exception):
    pass


class DeportistaYaInscrito(Exception):
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
            print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
            i += 1

    def mostrar_ranking_por_deporte(self, deporte):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            if (dep.deporte == deporte):
                print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
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
                print(dep)
                return
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

        if deportista in self.participantes:
            raise DeportistaYaInscrito(f"{deportista.nombre} ya está inscrito en la competencia.")
        
        for dep in self.registro.deportistas:
            if (deportista.nombre == dep.nombre):
                if(deportista.deporte == self.deporte):
                    self.participantes.append(deportista)
                else:
                    raise DeporteIncorrecto(f"{deportista.nombre} practica {deportista.deporte}, no {self.deporte}.")
            else:
                raise DeportistaNoEncontrado(f"Deportista '{deportista.nombre}' no encontrado en el registro.")


    def registrar_resultado(self, resultado):
        #como es el parametro resultado, cada deportista y su puntaje? los primeros puestos? NO SÉ
        return
    
    def mostrar_resultado(self):
        return
    
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
        print(f"El rendimiento de {self.nombre} es de {rendimiento}.")
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
    def __init__(self, nombre, edad, puntaje, cantidad_de_competencias, disciplina, mejores_tiempos):
        super().__init__(nombre, edad, "Atletismo", puntaje, cantidad_de_competencias)

        if not disciplina:
            raise ErrorDatosInvalidos("La disciplina no puede estar vacía.")

        self.disciplina = disciplina
        self.mejores_tiempos = []

    def obtener_informacion_basica(self):
        super().obtener_informacion_basica()
        print(f"Disciplina: {self.disciplina}")
        print(f"Puntaje: {self.puntaje}")

    def agregar_mejores_tiempos(self, tiempo):
        if tiempo <= 0:
            raise ErrorDatosInvalidos("El tiempo debe ser mayor a 0.")

        self.mejores_tiempos.append(tiempo)

#falta implementar excepciones para manejar errores
#Si un jugador que pertenece a un equipo o dupla cambia de equipo, pierde sus 
# puntos personales; sin embargo, el equipo mantiene los puntos acumulados.

#en agregar mejores tiempos, que es marca valida??
#a que se refiere con ingresar resultado?? registrar o mostrar resultado?