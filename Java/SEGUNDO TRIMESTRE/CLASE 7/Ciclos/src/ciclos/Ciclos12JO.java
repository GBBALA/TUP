package ciclos;
import javax.swing.JOptionPane;

public class Ciclos12JO {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        //System.out.println("El factorial del numero ingresado es " + factorial);
        JOptionPane.showMessageDialog(null, "El factorial del numero ingresado es: " + factorial);
    }
}
