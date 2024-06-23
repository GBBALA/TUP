import java.util.Scanner;

public class Clase10Leccion2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        boolean condicion = false;

        if (condicion) {
            System.out.println("Condición Verdadera"); // Condicional simple
        } else {
            System.out.println("Condición Falsa"); // Condicional doble
        }
        var numero = 2;
        var nummeroTexto = "Número desconocido";
        if (numero == 1) {
            nummeroTexto = "Numero uno";
        }
        else if (numero == 2) {
            nummeroTexto = "Numero dos";
        }
        else if (numero == 3) {
            nummeroTexto = "Numero tres";
        }
        else if (numero == 4) {
            nummeroTexto = "Numero cuatro";
        }
        else{
            nummeroTexto = "Numero no encontrado";
        }
        System.out.println("numeroTexto = " + nummeroTexto);
    }
}
