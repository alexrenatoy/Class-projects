from encapsulamiento import Persona

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
    
exports = [Estudiante]