import java.util.ArrayList;
import java.util.List;

public class Admin extends Usuario {
    private List<String> permisos;

    public Admin(String nombre, int edad, String sexo, List<String> permisos) {
        super(nombre, edad, sexo, "Administrador");
        this.permisos = permisos;
    }

    @Override
    public String describir() {
        return "Admin: " + nombre + ", Edad: " + edad + ", Permisos: " + String.join(", ", permisos);
    }

    public void agregarPermiso(String permiso) {
        permisos.add(permiso);
    }

    public String mostrarPermisos() {
        return "Permisos de " + nombre + ": " + String.join(", ", permisos);
    }
}
