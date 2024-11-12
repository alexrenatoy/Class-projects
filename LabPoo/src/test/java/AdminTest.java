import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AdminTest {
    private Admin admin;

    @BeforeEach
    public void setUp() {
        admin = new Admin("María", 35, "Femenino", new ArrayList<>());
        admin.agregarPermiso("Gestionar usuarios");
        admin.agregarPermiso("Configurar sistema");
    }

    @Test
    public void testDescribir() {
        String expectedDescription = "Admin: María, Edad: 35, Permisos: Gestionar usuarios, Configurar sistema";
        System.out.println(expectedDescription);
        assertEquals(expectedDescription, admin.describir());
    }

    @Test
    public void testAgregarPermiso() {
        admin.agregarPermiso("Auditar");
        String expectedPermisos = "Permisos de María: Gestionar usuarios, Configurar sistema, Auditar";
        System.out.println(expectedPermisos);
        assertEquals(expectedPermisos, admin.mostrarPermisos());
    }
}
