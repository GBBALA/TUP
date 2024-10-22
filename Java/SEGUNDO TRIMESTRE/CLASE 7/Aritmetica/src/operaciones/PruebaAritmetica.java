package operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //Variables Locales
        int b = 7;
        miMetodo();
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b =7;
        //aritmetica1 = null;
        aritmetica1.sumarNumeros ();

        //Para almacenar un objeto o los atributos wse utiliza la memoria heap

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+ resultado);
        System.out.println("aritmetica1 b: " +aritmetica1.b);


        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2.a = " + aritmetica2.a);
        System.out.println("aritmetica2.b = " + aritmetica2.b);
       // aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); metodo para limpiar resuidos, es pesado no utilizar



    }

    public static void miMetodo(){
       // a = 10; una variable esta limitada
        System.out.println("Aqui tenemos otro metodo");
    }
    class Persona{
        String nombre;
        String apellido;

        Persona(String nombre, String apellido){
            super();
            //Imprimir imprimir = new Imprimir();
            new Imprimir().imprimir(this);

            this.nombre = nombre;
            this.apellido = apellido;
            System.out.println("Objeto persona usando this: "+this);
        }

    }
    class Imprimir {
        public Imprimir() {
            super(); // el constructor de la clase padre, para reservar memoria
        }

        public void imprimir(Persona persona) {
            System.out.println("Persona desde la clase imprimir "+persona);
            System.out.println("Impresion del obnjeto actual (this): "+this);
        }
    }
}
