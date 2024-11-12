export interface Humano {
    nombre: string;
    edad: number;
    sexo: string;
    language(): void;
}

export interface IUsuario {
    nombre: string;
    edad: number;
    sexo: string;
    rol: string;    
    describir(): string;
  }