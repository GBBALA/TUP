import java.util.Scanner;

public class Ejercicio3Switch {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número entre 0 y 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());

        switch (calificacion) {
            case 10:
            case 9:
                System.out.println("A");
                break;
            case 8:
                System.out.println("B");
                break;
            case 7:
                System.out.println("C");
                break;
            case 6:
                System.out.println("D");
                break;
            default:
                System.out.println("Fuera de rango");
                break;
        }
    }
}
