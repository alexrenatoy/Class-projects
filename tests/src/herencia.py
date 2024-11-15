# herencia.py
from encapsulamiento import Persona, Planta

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

class Arbol(Planta):
    def __init__(self, nombre: str, origen: str, clima: str, altura: int):
        super().__init__(nombre, origen, clima)
        self.__altura = altura

    def get_altura(self) -> int:
        return self.__altura

    def set_altura(self, altura: int) -> None:
        self.__altura = altura

    def exponer(self) -> str:
        return f"Soy un arbol, me llamo {self.get_nombre()} y mi altura es {self.__altura}."