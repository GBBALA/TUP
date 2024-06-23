let parInpar = 10;

if (parInpar % 2 === 0) {
    console.log("Es un número PAR");
} else {
    console.log("Es un número IMPAR");
}

// Ejercicio: Es mayor de edad
let edad = 18;
const adulto = 18;

if (edad >= adulto) {
    console.log("Usted es una persona adulta");
} else {
    console.log("Usted es una persona menor de edad");
}

let valor = 20; // Aquí vamos a ir cambiando el valor
let valMin = 10, valMax = 100;
if (valor >= valMin && valor <= valMax) {
    console.log('El valor dentro del rango es válido');
} else {
    console.log('Está fuera del rango establecido');
}

// Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo");
} else {
    console.log("El padre no puede asistir al juego de su hijo");
}
//Convertir String a Number
let miNumero = "21"; // Es una cadena
console.log(typeof miNumero);

let edad2 = Number(miNumero); // Esta es una función
console.log(typeof edad2);
if(isNaN(edad2)){
    console.log("Esta variable no contiene solo numeros ")
}
else{
    if (edad2 >= 18) {
        console.log("Puede votar");
    } else {
        console.log("Muy joven para votar");
    }

}
if (edad2 >= 18) {
    console.log("Puede votar");
} else {
    console.log("Muy joven para votar");
}

// Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);
