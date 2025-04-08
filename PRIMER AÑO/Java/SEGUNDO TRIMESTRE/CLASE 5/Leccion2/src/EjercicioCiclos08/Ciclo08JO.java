package EjercicioCiclos08;

import javax.swing.JOptionPane;

public class Ciclo08JO {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        int i = 1;
        while (i <= numero) {
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}
