import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1, nota2, nota3, suma;

        System.out.println("Digite tres notas o calificaciones: ");
        // Leemos las tres notas ingresadas por el usuario
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());

        // Calculamos la suma de las tres notas
        suma = nota1 + nota2 + nota3;

        System.out.println("\nLa suma es: " + suma);
    }
}