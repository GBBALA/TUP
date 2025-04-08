// while
let contador = 0;

while(contador < 3) {
  console.log(contador); 
  contador++;
}

console.log("Fin del ciclo while");

//do while
let conteo = 0;
do{
    console.log(conteo); 0, 1, 2
    conteo++;
}while(conteo < 3);
console.log("fin del ciclo do while")

//for
for(let contando = 0; contando <3; contando++){
    console.log(contando); 
}
console.log("fin del ciclo for")
// Palabra reservada break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer número par")
// La palabra continue y etiquetas labels
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 === 0) {
      continue; // ir a la siguiente iteración
    }
    console.log(contando); // 0, 2, 4, 6, 8, 10
  }
  console.log("Termina el ciclo");