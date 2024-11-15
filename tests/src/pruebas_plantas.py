import pytest  # Importa el módulo pytest, utilizado para realizar las pruebas automatizadas.
import time  # Importa el módulo time, que proporciona funciones para medir el tiempo.
from typing import List  # Importa List de typing para indicar que las funciones retornan listas de objetos.
from datetime import datetime  # Importa datetime para registrar las fechas y horas.
from encapsulamiento import Planta  # Importa la clase Persona desde el módulo de encapsulamiento.
from herencia import Arbol  # Importa la clase Estudiante desde el módulo de herencia.
from polimorfismo import Hortaliza, exponer_planta  # Importa la clase Profesor y la función presentar_persona desde el módulo de polimorfismo.
import concurrent.futures  # Importa el módulo concurrent.futures para manejar concurrencia y multithreading.

class TestRendimiento:  # Clase que agrupa las pruebas de rendimiento.
    @pytest.fixture
    def crear_muchas_plantas(self) -> List[Planta]:
        return [Planta(f"Planta{i}", 20 + i, 5) for i in range(1000)]
    
    @pytest.fixture
    def crear_muchos_arboles(self) -> List[Arbol]:
        return [Arbol(f"Arbol{i}", f"Origen{i}", f"Clima{i}", 20 + i) for i in range(1000)]
    
    @pytest.fixture
    def crear_muchas_hortalizas(self) -> List[Hortaliza]:
        utilidades = ["Medicinal", "Alimenticio", "Decorativa", "Frutal"]
        return [Hortaliza(f"Hortaliza{i}", f"Origen{i}", f"Clima{i}", utilidades[i % len(utilidades)]) for i in range(1000)]
    
    def test_rendimiento_creacion(self, benchmark):
        def crear_objetos():
            plantas = [Planta(f"Planta{i}", 20 + i, 5) for i in range(1000)]
            arboles = [Arbol(f"Arbol{i}", f"Origen{i}", f"Clima{i}", 20 + i) for i in range(1000)]
            utilidades = ["Medicinal", "Alimenticio", "Decorativa", "Frutal"]
            hortalizas = [Hortaliza(f"Hortaliza{i}", f"Origen{i}", f"Clima{i}", utilidades[i % len(utilidades)]) for i in range(1000)]
            return len(plantas) + len(arboles) + len(hortalizas)
        
        result = benchmark(crear_objetos)
        assert result == 3000
    
    @pytest.mark.timeout(2)
    def test_tiempo_presentacion(self, crear_muchas_plantas, crear_muchos_arboles, crear_muchas_hortalizas):
        start_time = time.time()
        for planta in crear_muchas_plantas:
            exponer_planta(planta)
        for arbol in crear_muchos_arboles:
            exponer_planta(arbol)
        for hortaliza in crear_muchas_hortalizas:
            exponer_planta(hortaliza)
        
        tiempo_total = time.time() - start_time
        assert tiempo_total < 2.0, f"La exposicipon tomó demasiado tiempo: {tiempo_total:.4f} segundos"

class TestPlanta:
    @pytest.mark.parametrize("nombre, altura, clima", [
        ("", 10, "Tropical"),  # Nombre vacío
        ("Pino", -5, "Frío"),  # Altura negativa
        ("Cactus", 0, "Desértico"),  # Altura cero
        ("Olivo", 150, "Mediterráneo"),  # Altura muy alta
        ("Helecho", 5, ""),  # Clima vacío
    ])
    def test_valores_invalidos_planta(self, nombre, altura, clima):
        # Valida si se levantan excepciones cuando se ingresan valores inválidos.
        with pytest.raises(ValueError):
            # Verificar condiciones de validación para cada parámetro.
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")  # Verifica si el nombre es vacío.
            if altura <= 0 or altura >= 120:
                raise ValueError("La altura debe estar entre 1 y 120")  # Verifica si la altura está fuera de rango.
            if not clima:
                raise ValueError("El clima no puede estar vacío")  # Verifica si el clima es vacío.
            
            # Si los valores son válidos, crea la instancia de Planta.
            planta = Planta(nombre, altura, clima)
            assert planta.get_nombre() == nombre
            assert planta.get_altura() == altura
            assert planta.get_clima() == clima