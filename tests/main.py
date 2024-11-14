from encapsulamiento import Persona
from herencia import Estudiante
from polimorfismo import Estudiante, Profesor, presentar_persona

if __name__ == "__main__":
    persona = Persona('Juan', 20)
    presentar_persona(persona)

    estudiante = Estudiante('Pedro', 22, 'Informatica')
    presentar_persona(estudiante)

    profesor = Profesor('Maria', 30, 'Matematicas')
    presentar_persona(profesor)

    profesor.set_materia('Fisica')
    presentar_persona(profesor)

    estudiante.set_carrera('Informatica')
    presentar_persona(estudiante)

    