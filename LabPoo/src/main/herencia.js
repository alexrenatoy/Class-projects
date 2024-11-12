"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Admin = exports.Estudiante = void 0;
const encapsulamiento_1 = require("./encapsulamiento");
class Estudiante extends encapsulamiento_1.Persona {
    constructor(nombre, edad, sexo, matricula) {
        super(nombre, edad, sexo);
        this.matricula = matricula;
    }
    getMatricula() {
        return this.matricula;
    }
    setMatricula(matricula) {
        this.matricula = matricula;
    }
}
exports.Estudiante = Estudiante;
class Admin extends encapsulamiento_1.Usuario {
    constructor(nombre, edad, sexo, permisos) {
        super(nombre, edad, sexo, 'Administrador');
        this.permisos = permisos;
    }
    describir() {
        return `Admin: ${this.nombre}, Edad: ${this.edad}, Permisos: ${this.permisos.join(', ')}`;
    }
    agregarPermiso(permiso) {
        this.permisos.push(permiso);
    }
    mostrarPermisos() {
        return `Permisos de ${this.nombre}: ${this.permisos.join(', ')}`;
    }
}
exports.Admin = Admin;
