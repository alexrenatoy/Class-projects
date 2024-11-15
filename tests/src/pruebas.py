# pruebas.py
import pytest
from encapsulamiento import Persona, Planta
from herencia import Estudiante, Arbol
from polimorfismo import Profesor, presentar_persona, exponer_planta, Hortaliza

class TestPersona:
    @pytest.fixture
    def persona(self):
        return Persona("Carlos", 30)
    
    def test_get_nombre_edad(self, persona):
        assert persona.get_nombre() == "Carlos"
        assert persona.get_edad() == 30
    
    def test_set_nombre_edad(self, persona):
        persona.set_nombre("Juan")
        persona.set_edad(35)
        assert persona.get_nombre() == "Juan"
        assert persona.get_edad() == 35

class TestEstudiante:
    @pytest.fixture
    def estudiante(self):
        return Estudiante("Ana", 22, "2022001")
    
    def test_get_atributos(self, estudiante):
        assert estudiante.get_nombre() == "Ana"
        assert estudiante.get_edad() == 22
        assert estudiante.get_matricula() == "2022001"
    
    def test_set_matricula(self, estudiante):
        estudiante.set_matricula("2022002")
        assert estudiante.get_matricula() == "2022002"

class TestProfesor:
    @pytest.fixture
    def profesor(self):
        return Profesor("Luis", 40, "Matematicas")
    
    def test_get_atributos(self, profesor):
        assert profesor.get_nombre() == "Luis"
        assert profesor.get_edad() == 40
        assert profesor.get_materia() == "Matematicas"
    
    def test_set_materia(self, profesor):
        profesor.set_materia("Fisica")
        assert profesor.get_materia() == "Fisica"

class TestPresentarPersona:
    @pytest.fixture
    def personas(self):
        persona = Persona("Carlos", 30)
        estudiante = Estudiante("Ana", 22, "2022001")
        profesor = Profesor("Luis", 40, "Matematicas")
        return persona, estudiante, profesor
    
    def test_presentar_persona(self, personas):
        persona, estudiante, profesor = personas
        assert presentar_persona(persona) == "Soy Carlos y tengo 30 años."
        assert presentar_persona(estudiante) == "Soy el estudiante Ana y mi matricula es 2022001."
        assert presentar_persona(profesor) == "Soy el profesor Luis y enseño Matematicas."


class TestPlanta:
    @pytest.fixture
    def plantas(self):
        return Planta("Manzano", "Norte", "Frio")
    
    def test_get_nombre_origen_clima(self, plantas):
        assert plantas.get_nombre() == "Manzano"
        assert plantas.get_origen() == "Norte"
        assert plantas.get_clima() == "Frio"
    
    def test_set_nombre_origen_clima(self, plantas):
        plantas.set_nombre("Hortaliza")
        plantas.set_origen("Sur")
        plantas.set_clima("Calido")
        assert plantas.get_nombre() == "Hortaliza"
        assert plantas.get_origen() == "Sur"
        assert plantas.get_clima() == "Calido"

class TestArbol:
    @pytest.fixture
    def arbol(self):
        return Arbol("Manzano", "Norte", "Frio", 10)
    
    def test_get_atributos(self, arbol):
        assert arbol.get_nombre() == "Manzano"
        assert arbol.get_origen() == "Norte"
        assert arbol.get_clima() == "Frio"
        assert arbol.get_altura() == 10

    def test_set_altura(self, arbol):
        arbol.set_altura(20)
        assert arbol.get_altura() == 20

class TestHortaliza:
    @pytest.fixture
    def hortaliza(self):
        return Hortaliza("Hortaliza", "Norte", "Frio", 10)
    
    def test_get_atributos(self, hortaliza):
        assert hortaliza.get_nombre() == "Hortaliza"
        assert hortaliza.get_origen() == "Norte"
        assert hortaliza.get_clima() == "Frio"
        assert hortaliza.get_altura() == 10
    
    def test_set_utilidad(self, hortaliza):
        hortaliza.set_utilidad("Alimentos")
        assert hortaliza.get_utilidad() == "Alimentos"

class TestExponerPlanta:
    @pytest.fixture
    def plantas(self):
        planta = Planta("Manzano", "Norte", "Frio")
        arbol = Arbol("Manzano", "Norte", "Frio", 10)
        hortaliza = Hortaliza("Hortaliza", "Norte", "Frio", 10)
        return planta, arbol, hortaliza
    
    def test_exponer_planta(self, plantas):
        planta, arbol, hortaliza = plantas
        assert exponer_planta(planta) == "Soy una planta, me llamo Naranjo y mi origen es Norte."
        assert exponer_planta(arbol) == "Soy una planta, me llamo Manzano y mi origen es Norte."
        assert exponer_planta(hortaliza) == "Soy una hortaliza, me llamo Apio y mi origen es Norte."
