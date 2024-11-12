"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Usuario = exports.Persona = void 0;
class Persona {
    constructor(nombre, edad, sexo) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
    }
    language() {
        console.log('Todos somos iguales c:');
    }
    getNombre() {
        return this.nombre;
    }
    getEdad() {
        return this.edad;
    }
    getSexo() {
        return this.sexo;
    }
    setNombre(nombre) {
        this.nombre = nombre;
    }
    setEdad(edad) {
        this.edad = edad;
    }
    setSexo(sexo) {
        this.sexo = sexo;
    }
}
exports.Persona = Persona;
class Usuario {
    constructor(nombre, edad, sexo, rol) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        this.rol = rol;
    }
    static saludar() {
        return 'Bienvenido al sistema de usuarios';
    }
}
exports.Usuario = Usuario;
