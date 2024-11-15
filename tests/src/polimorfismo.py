from encapsulamiento import Persona, Planta
from herencia import Estudiante, Arbol

class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, materia: str):
        super().__init__(nombre, edad)
        self.__materia = materia
    
    def get_materia(self) -> str:
        return self.__materia
    
    def set_materia(self, materia: str) -> None:
        self.__materia = materia
    
    def presentar(self) -> str:
        return f"Soy el profesor {self.get_nombre()} y enseño {self.__materia}."

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, matricula: str):
        super().__init__(nombre, edad)
        self.__matricula = matricula

    def get_matricula(self) -> str:
        return self.__matricula

    def set_matricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def presentar(self) -> str:
        return f"Soy el estudiante {self.get_nombre()} y mi matricula es {self.__matricula}."
    
class Hortaliza(Planta):
    def __init__(self, nombre: str, origen: str, clima: str, utilidad: str):
        super().__init__(nombre, origen, clima)
        self.__utilidad = utilidad

    def get_utilidad(self) -> str:
        return self.__utilidad

    def set_utilidad(self, utilidad: str) -> None:
        self.__utilidad = utilidad

    def exponer(self) -> str:
        return f"Soy una hortaliza, me llamo {self.get_nombre()} y mi utilidad es {self.__utilidad}."

class Arbol(Planta):
    def __init__(self, nombre: str, origen: str, clima: str, altura: int):
        super().__init__(nombre, origen, clima)
        self.__altura = altura

    def get_altura(self) -> int:
        return self.__altura

    def set_altura(self, altura: int) -> None:
        self.__altura = altura

    def exponer(self) -> str:
        return f"Soy un arbol, me llamo {self.get_nombre()} y mi altura es {self.__altura} m."


def exponer_planta(planta: Planta) -> str:
    return planta.exponer()

def presentar_persona(persona: Persona) -> str:
    return persona.presentar()