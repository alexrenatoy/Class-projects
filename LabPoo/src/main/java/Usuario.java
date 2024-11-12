public abstract class Usuario implements IUsuario {
    protected String nombre;
    protected int edad;
    protected String sexo;
    protected String rol;
    
    public Usuario(String nombre, int edad, String sexo, String rol) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        this.rol = rol;
    }

    public static String saludar() {
        return "Bienvenido al sistema de usuarios";
    }    
    public String getNombre() { 
        return nombre;
        }
    public int getEdad() { 
        return edad; 
        }
    public String getSexo() { 
        return sexo;
        }
    public String getRol() { 
        return rol; 
        }

    public abstract String describir();
}
