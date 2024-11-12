import { Persona } from './encapsulamiento';

class Profesor extends Persona {
    private materia: string;

    constructor(nombre: string, edad: number, sexo: string, materia: string) {
        super(nombre, edad, sexo);
        this.materia = materia;
    }

    public getMateria(): string {
        return this.materia;
    }

    public setMateria(materia: string): void {
        this.materia = materia;
    }

    public presentar(): string {
        return `Soy el profesor ${this.getNombre()} y enseño ${this.materia}.`;
    }
}

class Estudiante extends Persona {
    private matricula: string;

    constructor(nombre: string, edad: number,sexo: string, matricula: string) {
        super(nombre, edad, sexo);
        this.matricula = matricula;
    }

    public getMatricula(): string {
        return this.matricula;
    }

    public setMatricula(matricula: string): void {
        this.matricula = matricula;
    }

    public presentar(): string {
        return `Soy el estudiante ${this.getNombre()} y mi matrícula es ${this.matricula}.`;
    }
}

function presentarPersona(persona: Persona): string {
    if (persona instanceof Profesor) {
        return persona.presentar();
    } else if (persona instanceof Estudiante) {
        return persona.presentar();
    } else {
        return `Soy ${persona.getNombre()} y tengo ${persona.getEdad()} años.`;
    }
}

export { Profesor, Estudiante, presentarPersona };