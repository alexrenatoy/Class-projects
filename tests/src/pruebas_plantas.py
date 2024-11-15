import pytest  # Importa el módulo pytest, utilizado para realizar las pruebas automatizadas.
import time  # Importa el módulo time, que proporciona funciones para medir el tiempo.
from typing import List  # Importa List de typing para indicar que las funciones retornan listas de objetos.
from datetime import datetime  # Importa datetime para registrar las fechas y horas.
from encapsulamiento import Planta  # Importa la clase Persona desde el módulo de encapsulamiento.
from herencia import Arbol  # Importa la clase Estudiante desde el módulo de herencia.
from polimorfismo import Hortaliza, presentar_persona  # Importa la clase Profesor y la función presentar_persona desde el módulo de polimorfismo.
import concurrent.futures  # Importa el módulo concurrent.futures para manejar concurrencia y multithreading.

class TestRendimiento:  # Clase que agrupa las pruebas de rendimiento.
    @pytest.fixture
    def crear_muchas_plantas(self) -> List[Planta]:
        return [Planta(f"Planta{i}", 20 + i + i) for i in range(1000)]
    
    @pytest.fixture
    def crear_muchos_arboles(self) -> List[Arbol]:
        return [Arbol(f"Arbol{i}", 20 + i, f"MAT{i:04d}") for i in range(1000)]
    
    @pytest.fixture
    def crear_muchas_hortalizas(self) -> List[Hortaliza]:
        utilidades = ["Medicinal", "Alimenticio", "Decorativa", "Frutal"]
        return [Hortaliza(f"Hortaliza{i}", 20 + i, utilidades[i % len(utilidades)]) for i in range(1000)]
    
    def test_rendimiento_creacion(self, benchmark):
        def crear_objetos():
            plantas = [Planta(f"Planta{i}", 20 + i) for i in range(1000)]
            arboles = [Arbol(f"Arbol{i}", 20 + i, f"MAT{i:04d}") for i in range(1000)]
            hortalizas = [Hortaliza(f"Hortaliza{i}", 20 + i, "Medicinal") for i in range(1000)]
            return len(plantas) + len(arboles) + len(hortalizas)
        
        result = benchmark(crear_objetos)
        assert result == 3000
    
    @pytest.mark.timeout(2)
    def test_tiempo_presentacion(self, crear_muchas_plantas, crear_muchos_arboles, crear_muchas_hortalizas):
        start_time = time.time()
        for planta in crear_muchas_plantas:
            presentar_persona(planta)
        for arbol in crear_muchos_arboles:
            presentar_persona(arbol)
        for hortaliza in crear_muchas_hortalizas:
            presentar_persona(hortaliza)
        
        tiempo_total = time.time()
        assert tiempo_total < 2.0, f"La exposicipon tomó demasiado tiempo: {tiempo_total:.4f} segundos"

class TestPlanta:

    @pytest.mark.parametrize("nombre,altura,clima", [("Manzano", 10, "Frio"), ("Arbol", 20, "Tropical"), ("Hortaliza", 5, "Frio")])
    
    def test_get_atributos(self, nombre, altura, clima):
        with pytest.raises(ValueError):
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            if altura <= 0 or altura >= 120:
                raise ValueError("La altura debe estar entre 1 y 120")
            if not clima:
                raise ValueError("El clima no puede estar vacío")
            planta = Planta(nombre, altura, clima)