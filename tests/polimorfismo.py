from encapsulamiento import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def saludar(self):
        print(f'Hola, soy {self.get_nombre()} y enseño {self.materia}.')

    def get_materia(self):
        return self.materia

    def set_materia(self, materia):
        self.materia = materia

    


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def saludar(self):
        print(f'Hola, soy {self.get_nombre()} y estudio {self.carrera}.')

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera


def presentar_persona(persona):
    if isinstance(persona, Profesor):
        persona.saludar()
        print(f'Estoy presentando a un profesor: {persona.get_nombre()}')
    elif isinstance(persona, Estudiante):
        persona.saludar()    
        print(f'Estoy presentando a un estudiante: {persona.get_nombre()}')

export = [presentar_persona, Profesor, Estudiante]