import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(Usuario.saludar());

        Admin admin = new Admin("María", 35, "Femenino", Arrays.asList("Gestionar usuarios", "Configurar sistema"));
        System.out.println(admin.describir());
        admin.agregarPermiso("Auditar");
        System.out.println(admin.mostrarPermisos());
    }
}
