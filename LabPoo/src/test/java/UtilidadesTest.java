import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UtilidadesTest {

    @Test
    public void testPresentarPersona() {
        Persona persona = new Persona("Carlos", 30, "Masculino");
        String expectedOutput = "Presentando a Carlos, 30 años, de género Masculino";
        System.out.println(expectedOutput);
        System.out.println(Utilidades.presentarPersona(persona));
        assertEquals(expectedOutput, Utilidades.presentarPersona(persona));
    }
}

