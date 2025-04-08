import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double nota1, nota2, nota3, promedio;

        System.out.println("Digite la primera calificación:");
        nota1 = input.nextDouble();

        System.out.println("Digite la segunda calificación:");
        nota2 = input.nextDouble();

        System.out.println("Digite la tercera calificación:");
        nota3 = input.nextDouble();

        promedio = (nota1 + nota2 + nota3) / 3;

        if (promedio >= 7) {
            System.out.println("El alumno está aprobado con un promedio de: " + promedio);
        } else {
            System.out.println("El alumno está desaprobado con un promedio de: " + promedio);
        }
    }
}
