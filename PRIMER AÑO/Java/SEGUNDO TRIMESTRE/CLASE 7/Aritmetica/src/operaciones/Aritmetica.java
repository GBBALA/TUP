package operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //El constructor es un metodo especial
    public Aritmetica(){
        System.out.println("Se esta ejecutando este constructor");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores

    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor número dos");

    }

    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado= " + resultado);
    }

    public int sumarConRetorno (){
        //int resultado = a + b;
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a; //el atributo a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return sumarConRetorno();
    }
}
