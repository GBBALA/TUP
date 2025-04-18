/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero
para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;
import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;

        // Leer números hasta que se introduzca un cero
        System.out.println("Introduce un número (0 para salir):");
        numero = scanner.nextInt();

        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El número " + numero + " es par.");
            } else {
                System.out.println("El número " + numero + " es impar.");
            }

            System.out.println("Introduce otro número (0 para salir):");
            numero = scanner.nextInt();
        }

        System.out.println("Has introducido el número 0. Fin del programa.");
        scanner.close();
    }
}
