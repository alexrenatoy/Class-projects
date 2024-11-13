public class Estudiante extends Persona {
    private String matricula;

    public Estudiante(String nombre, int edad, String sexo, String matricula) {
        super(nombre, edad, sexo);
        this.matricula = matricula;
    }

    public String getMatricula() {
        return matricula;
    }
}
