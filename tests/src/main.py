# main.py
from encapsulamiento import Persona, Planta
from herencia import Estudiante, Arbol
from polimorfismo import Profesor, presentar_persona, exponer_planta, Hortaliza

if __name__ == "__main__":
    persona = Persona('Carlos', 30)
    print(f"Persona: {persona.get_nombre()}, {persona.get_edad()} anios")
    
    estudiante = Estudiante('Ana', 22, '2022001')
    print(f"Estudiante: {estudiante.get_nombre()}, {estudiante.get_edad()} anios, Matricula: {estudiante.get_matricula()}")
    
    profesor = Profesor('Luis', 40, 'Matematicas')
    print(f"Profesor: {profesor.get_nombre()}, {profesor.get_edad()} anios, Materia: {profesor.get_materia()}")
    
    print(presentar_persona(persona))
    print(presentar_persona(estudiante))
    print(presentar_persona(profesor))

    planta = Planta('Arbol', 'Norte', 'Frio')
    print(f"Planta: {planta.get_nombre()}, Ubicacion: {planta.get_origen()}, Clima: {planta.get_clima()}")

    arbol = Arbol('Arbol', 'Norte', 'Frio', 10)
    print(f"Arbol: {arbol.get_nombre()}, Ubicacion: {arbol.get_origen()}, Clima: {arbol.get_clima()}, Altura: {arbol.get_altura()}")

    hortaliza = Hortaliza('Hortaliza', 'Norte', 'Frio', 10)
    print(f"Hortaliza: {hortaliza.get_nombre()}, Ubicacion: {hortaliza.get_origen()}, Clima: {hortaliza.get_clima()}, Altura: {hortaliza.get_altura()}")

    print(exponer_planta(planta))
    print(exponer_planta(arbol))
    print(exponer_planta(hortaliza))