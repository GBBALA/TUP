import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float franco, jorge, juan, total;

        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        franco = Float.parseFloat(entrada.nextLine());

        jorge = franco / 2;
        juan = (jorge + franco) / 2;
        total = jorge + franco + juan;

        System.out.println("\nEl dinero de Luis es: $" + jorge);
        System.out.println("El dinero de Juan es: $" + juan);
        System.out.println("El total de dinero entre los tres es: $" + total);
    }
}