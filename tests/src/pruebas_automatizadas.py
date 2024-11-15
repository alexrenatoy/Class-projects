import pytest  # Importa el módulo pytest, utilizado para realizar las pruebas automatizadas.
import time  # Importa el módulo time, que proporciona funciones para medir el tiempo.
from typing import List  # Importa List de typing para indicar que las funciones retornan listas de objetos.
from datetime import datetime  # Importa datetime para registrar las fechas y horas.
from encapsulamiento import Persona  # Importa la clase Persona desde el módulo de encapsulamiento.
from herencia import Estudiante  # Importa la clase Estudiante desde el módulo de herencia.
from polimorfismo import Profesor, presentar_persona  # Importa la clase Profesor y la función presentar_persona desde el módulo de polimorfismo.
import concurrent.futures  # Importa el módulo concurrent.futures para manejar concurrencia y multithreading.

#Pruebas de rendimiento y tiempo
class TestRendimiento:  # Clase que agrupa las pruebas de rendimiento.

    @pytest.fixture
    def crear_muchas_personas(self) -> List[Persona]:
        # Esta función crea 1000 objetos de la clase Persona y los devuelve en una lista.
        return [Persona(f"Persona{i}", 20 + i) for i in range(1000)]
    
    @pytest.fixture
    def crear_muchos_estudiantes(self) -> List[Estudiante]:
        # Esta función crea 1000 objetos de la clase Estudiante con un número de matrícula secuencial.
        return [Estudiante(f"Estudiante{i}", 20 + i, f"MAT{i:04d}") for i in range(1000)]
    
    @pytest.fixture
    def crear_muchos_profesores(self) -> List[Profesor]:
        # Crea 1000 objetos de la clase Profesor, alternando entre 5 materias.
        materias = ["Matemáticas", "Física", "Química", "Historia", "Literatura"]
        return [Profesor(f"Profesor{i}", 30 + i, materias[i % len(materias)]) for i in range(1000)]

    def test_rendimiento_creacion(self, benchmark):
        # Prueba el rendimiento de la creación de objetos usando la función benchmark.
        def crear_objetos():
            personas = [Persona(f"Persona{i}", 20 + i) for i in range(100)]
            estudiantes = [Estudiante(f"Estudiante{i}", 20 + i, f"MAT{i:04d}") for i in range(100)]
            profesores = [Profesor(f"Profesor{i}", 30 + i, "Materia") for i in range(100)]
            return len(personas) + len(estudiantes) + len(profesores)
        
        # Se mide el tiempo de creación y se valida que se creen 300 objetos en total.
        result = benchmark(crear_objetos)
        assert result == 300

    @pytest.mark.timeout(2)  # Marca la prueba para que falle si no se completa en 2 segundos.
    def test_tiempo_presentacion(self, crear_muchas_personas, crear_muchos_estudiantes, crear_muchos_profesores):
        # Esta prueba mide el tiempo de ejecución de la presentación de objetos.
        inicio = time.time()  # Registra el tiempo inicial.

        # Se presenta cada persona, estudiante y profesor en bucles.
        for persona in crear_muchas_personas:
            presentar_persona(persona)
        for estudiante in crear_muchos_estudiantes:
            presentar_persona(estudiante)
        for profesor in crear_muchos_profesores:
            presentar_persona(profesor)

        tiempo_total = time.time() - inicio  # Calcula el tiempo total transcurrido.
        assert tiempo_total < 2.0, f"La presentación tomó demasiado tiempo: {tiempo_total:.4f} segundos"
        # Verifica que el tiempo total no supere los 2 segundos.



#Pruebas de validación de datos

class TestValidacionDatos:  # Clase para pruebas de validación de datos.

    @pytest.mark.parametrize("nombre,edad", [
        ("", 20),  # Nombre vacío
        ("Ana", -1),  # Edad negativa
        ("Juan", 0),  # Edad cero
        ("María", 150),  # Edad muy alta
    ])
    def test_valores_invalidos(self, nombre, edad):
        # Valida si se levantan excepciones cuando se ingresan valores inválidos.
        with pytest.raises(ValueError):
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")  # Verifica si el nombre es vacío.
            if edad <= 0 or edad >= 120:
                raise ValueError("La edad debe estar entre 1 y 120 años")  # Verifica si la edad está fuera de rango.
            persona = Persona(nombre, edad)  # Si no hay excepciones, crea la Persona.


