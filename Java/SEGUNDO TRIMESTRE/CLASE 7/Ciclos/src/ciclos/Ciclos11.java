/*
Ejercicio 11: Diseñar un progama que muestre el producto
de los 10 primeros números impares
Hacerlo con JOptioPane
 */
package ciclos;
import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for (int i = 1; i <= 5; i += 2) {
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los números impares es " + producto);
    }
}
