import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PersonaTest {

    @Test
    public void testGetNombre() {
        Persona persona = new Persona("Carlos", 30, "Masculino");        
        assertEquals("Carlos", persona.getNombre());
    }

    @Test
    public void testGetEdad() {
        Persona persona = new Persona("Carlos", 30, "Masculino");
        assertEquals(30, persona.getEdad());
    }

    @Test
    public void testGetSexo() {
        Persona persona = new Persona("Carlos", 30, "Masculino");
        assertEquals("Masculino", persona.getSexo());
    }
}
