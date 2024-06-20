import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double num1, num2, resultado;

        System.out.println("Digite dos números:");
        num1 = entrada.nextDouble();
        num2 = entrada.nextDouble();

        if (num1 > num2) {
            resultado = num1 - num2;
        } else {
            resultado = 0;
        }

        System.out.println("El primer número es mayor. El resultado es: " + resultado);
    }
}
