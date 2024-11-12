import { Persona, Usuario } from './encapsulamiento';

class Estudiante extends Persona {
    private matricula: string;

    constructor(nombre: string, edad: number, sexo:string, matricula: string) {
        super(nombre, edad, sexo);
        this.matricula = matricula;
    }

    public getMatricula(): string {
        return this.matricula;
    }

    public setMatricula(matricula: string): void {
        this.matricula = matricula;
    }
}

class Admin extends Usuario {
    constructor(nombre: string, edad: number, sexo: string, private permisos: string[]) {
      super(nombre, edad, sexo, 'Administrador');
    }
  
    describir(): string {
      return `Admin: ${this.nombre}, Edad: ${this.edad}, Permisos: ${this.permisos.join(', ')}`;
    }
  
    agregarPermiso(permiso: string): void {
      this.permisos.push(permiso);
    }
  
    mostrarPermisos(): string {
      return `Permisos de ${this.nombre}: ${this.permisos.join(', ')}`;
    }
  }

export { Estudiante, Admin };