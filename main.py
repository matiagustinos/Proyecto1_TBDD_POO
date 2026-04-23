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
            else:
                print("Deportista no encontrado en registro.\n")



#return y break en una funcion o metodo cumplen la misma funcion?
#se pueden usar las propertys?