import { Humano, IUsuario } from "./interfaces";

class Persona implements Humano {
    public nombre: string;
    public edad: number;
    public sexo: string;        

    constructor(nombre: string, edad: number, sexo: string) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
    }
    public language(): void {
        console.log('Todos somos iguales c:')
    }

    public getNombre(): string {
        return this.nombre;
    }

    public getEdad(): number {
        return this.edad;
    }
    
    public getSexo(): string {
        return this.sexo;
    }

    public setNombre(nombre: string): void {
        this.nombre = nombre;
    }

    public setEdad(edad: number): void {
        this.edad = edad;
    }

    public setSexo(sexo: string): void {
        this.sexo = sexo;
    }    
}

abstract class Usuario implements IUsuario {
    constructor(
        public nombre: string, 
        public edad: number, 
        public sexo: string, 
        public rol: string
    ) {}
  
    abstract describir(): string;
  
    static saludar(): string {
      return 'Bienvenido al sistema de usuarios';
    }
  }

export { Persona, Usuario };