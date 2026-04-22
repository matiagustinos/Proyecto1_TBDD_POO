class Deportista:
    def __init__(self, nombre, edad, deporte, puntaje, cantidad_de_competencias):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.__puntaje = puntaje
        self.__cantidad_de_competencias = cantidad_de_competencias

    def obtener_informacion_basica(self):
        print(f"{self.nombre} realiza: {self.deporte}")

    def obtener_estadisticas(self):
        print(f"El deportista {self.nombre} tiene:")
        print(f"Puntaje -> {self.__puntaje}")
        print(f"Cantidad de competencias -> {self.__cantidad_de_competencias}")

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
                print("Deportista ya estaba registrado, por ende no se ingresó.")
                break
        self.deportistas.append(deportista)
    
    def mostrar_deportistas(self):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
            i =+ 1

    def mostrar_ranking_por_deporte(self, deporte):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            if (dep.deporte == deporte):
                print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
                i =+ 1
    
    def mostrar_n_mejores_deportistas(self, deporte, n):
        self.deportistas.sort(key=lambda d: d.puntaje, reverse=True)
        i = 1
        for dep in self.deportistas:
            if (dep.deporte == deporte and i <= n):
                print(f"{i}.- {dep.nombre} -> {dep.puntaje}\n")
                i =+ 1

    def buscar_deportista(self, nombre):
        for dep in self.deportistas:
            if (dep.nombre == nombre):
                obtener_informacion_basica()