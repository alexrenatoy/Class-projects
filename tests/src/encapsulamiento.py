# encapsulamiento.py
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self) -> str:
        return self.__nombre

    def get_edad(self) -> int:
        return self.__edad

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_edad(self, edad: int) -> None:
        self.__edad = edad

    def presentar(self) -> str:
        return f"Soy {self.get_nombre()} y tengo {self.get_edad()} años."
    
class Planta:
    def __init__(self, nombre: str, origen: str, clima: str):
        self.__nombre = nombre
        self.__origen = origen
        self.__clima = clima

    def get_nombre(self) -> str:
        return self.__nombre

    def get_origen(self) -> str:
        return self.__origen

    def get_clima(self) -> str:
        return self.__clima
    