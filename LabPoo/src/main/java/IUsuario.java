// export interface Humano {
//     nombre: string;
//     edad: number;
//     sexo: string;
//     language(): void;
// }

public interface IUsuario {
    String getNombre();
    int getEdad();
    String getSexo();
    String getRol();
    
    String describir();
}