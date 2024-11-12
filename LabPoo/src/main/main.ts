import { Persona, Usuario } from './encapsulamiento';
import { Admin, Estudiante } from './herencia';
import { Profesor, presentarPersona } from './polimorfismo';

console.log(Usuario.saludar());

const persona = new Persona('Carlos', 30, 'Masculino');
console.log(`Persona: ${persona.getNombre()}, ${persona.getEdad()} años, de genero ${persona.sexo}`);

const estudiante = new Estudiante('Ana', 22, 'Masculino', '2022001');
console.log(`Estudiante: ${estudiante.getNombre()}, ${estudiante.getEdad()} años, Matrícula: ${estudiante.getMatricula()} de genero ${estudiante.sexo}`);

const profesor = new Profesor('Luis', 40, 'Masculino', 'Matemáticas');
console.log(`Profesor: ${profesor.getNombre()}, ${profesor.getEdad()} años, Materia: ${profesor.getMateria()}, de genero ${profesor.sexo}`);

const human = new Persona('Alex', 23, 'Masculino');
console.log(`Persona: ${human.nombre}, ${human.getEdad()} años, de genero ${human.sexo}`);

const admin = new Admin('María', 35, 'Femenino', ['Gestionar usuarios', 'Configurar sistema']);

console.log(admin.describir());
admin.agregarPermiso('Auditor');
console.log(admin.mostrarPermisos());

console.log(presentarPersona(persona));
console.log(presentarPersona(estudiante));
console.log(presentarPersona(profesor));
console.log(presentarPersona(human));
