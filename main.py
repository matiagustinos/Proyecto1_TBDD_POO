class Deportista:
    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias):
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
        self.__puntaje += nuevo_puntaje
        self.__cantidad_de_competencias += 1 

class Registro:
    def __init__(self):
        self.deportistas = []

    def añadir_deportista(self, deportista):
        for dep in self.deportistas:
            if (dep == deportista):
                print("Deportista ya estaba registrado, por ende no se ingresó.\n")
                return
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
        print(f"Deportista '{nombre}' no encontrado en el registro.\n")

class Competencia:
    def __init__(self, nombre, fecha, participantes, resultados, deporte, registro):
        self.nombre = nombre
        self.fecha = fecha
        self.participantes = participantes
        self.resultados = resultados
        self.deporte = deporte
        self.registro = registro
    
    def inscribir_participantes(self, deportista):
        for dep in self.registro.deportistas:
            if (deportista.nombre == dep.nombre):
                if(deportista.deporte == self.deporte):
                    self.participantes.append(deportista)
                else:
                    print("No corresponde al deporte de la competencia.\n")
                    #error de consulta de datos
            else:
                print("Deportista no encontrado en registro.\n")
                #error de consulta de datos

    def registrar_resultado(self, resultado):
        #como es el parametro resultado, cada deportista y su puntaje? los primeros puestos? NO SÉ
        return
    
    def mostrar_resultado(self):
        return
    
    def mostrar_n_posiciones(self, n):
        self.participantes.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for deportista in self.participantes:
            if (i <= n):
                print(f"{i}.- {deportista.nombre} -> {deportista.puntaje}")
                i += 1
            else: return

class Futbolista(Deportista):
    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias, equipo, goles, asistencias, posicion):
        super().__init__(nombre, edad, "Futbol", puntaje, cantidad_de_competencias)
        self.equipo = equipo
        self.goles = goles
        self.asistencias = asistencias
        self.posicion = posicion

    def añadir_goles(self, goles):
        if (goles > 0):
            self.goles += goles
        else:
            print("El valor de goles a ingresar debe ser mayor a 0.")

    def añadir_asistencias(self, asistencias):
        if (asistencias > 0):
            self.asistencias += asistencias
        else:
            print("El valor de asistencias a ingresar debe ser mayor a 0.")

    def calcular_rendimiento(self):
        rendimiento = (self.goles*2 + self.asistencias*0.7)/self.__cantidad_de_competencias
        print(f"El rendimiento de {self.nombre} es de {rendimiento}.")
        return rendimiento

    def cambiar_de_equipo(self, nuevo_equipo):
        self.equipo = nuevo_equipo
        self.reiniciar_puntaje()

class Tenista(Deportista):
    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias, pareja, ranking_atp):
        super().__init__(nombre, edad, "Tenis", puntaje, cantidad_de_competencias)
        self.pareja = pareja
        self.ranking_atp = ranking_atp
    
    def actualizar_de_pareja(self, nueva_pareja):
        self.reiniciar_puntaje()
        self.pareja = nueva_pareja

class Atleta(Deportista):
    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias, disciplina, mejores_tiempos):
        super().__init__(nombre, edad, "Atletismo", puntaje, cantidad_de_competencias)
        self.disciplina = disciplina
        self.mejores_tiempos = []

    def agregar_mejores_tiempos(self, tiempo):
        if (tiempo > 0):
            self.mejores_tiempos.append(tiempo)

#falta metodo obtener_informacion_basica() para cada tipo de deportista
#falta implementar excepciones para manejar errores
#Si un jugador que pertenece a un equipo o dupla cambia de equipo, pierde sus 
# puntos personales; sin embargo, el equipo mantiene los puntos acumulados.

#en agregar mejores tiempos, que es marca valida??
#a que se refiere con ingresar resultado?? registrar o mostrar resultado?