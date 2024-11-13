import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(Usuario.saludar());

        Persona persona = new Persona("Carlos", 30, "Masculino");
        System.out.println("Persona: " + persona.getNombre() + ", " + persona.getEdad() + " años, de genero " + persona.getSexo());

        Estudiante estudiante = new Estudiante("Ana", 22, "Masculino", "2022001");
        System.out.println("Estudiante: " + estudiante.getNombre() + ", " + estudiante.getEdad() + " años, Matrícula: " + estudiante.getMatricula() + " de genero " + estudiante.getSexo());

        Profesor profesor = new Profesor("Luis", 40, "Masculino", "Matemáticas");
        System.out.println("Profesor: " + profesor.getNombre() + ", " + profesor.getEdad() + " años, Materia: " + profesor.getMateria() + ", de genero " + profesor.getSexo());

        Persona human = new Persona("Alex", 23, "Masculino");
        System.out.println("Persona: " + human.getNombre() + ", " + human.getEdad() + " años, de genero " + human.getSexo());

        Admin admin = new Admin("María", 35, "Femenino", Arrays.asList("Gestionar usuarios", "Configurar sistema"));

        System.out.println(admin.describir());
        admin.agregarPermiso("Auditor");
        System.out.println(admin.mostrarPermisos());

        System.out.println(Utilidades.presentarPersona(persona));
        System.out.println(Utilidades.presentarPersona(estudiante));
        System.out.println(Utilidades.presentarPersona(profesor));
        System.out.println(Utilidades.presentarPersona(human));
    }
}
