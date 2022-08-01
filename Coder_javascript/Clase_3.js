// MAPAS DE CONCEPTOS. CICLOS , BUCLES , FOR, WHILE, WHILE DO, ESTRUCTURA SWICH.

// FOR 
for (let i = 0 ; i < 11; i ++){ // ++ incremento en 1. -- decremento
    console.log(i)
}
for (let fila = 19; i > 0; i--){
    console.log(fila)
}


// SWITCH

let nombre_ingresado = prompt("Ingrese un nombre"); // LET DECLARA LA VARIABLE DESDE 0
while(nombre_ingresado != "ESC"){
    switch (nombre_ingresado){
        case "ANA":
            alert("HOLA ANA");
            break;
        case "JUAN":
            alert("HOLA JUAN");
            break;
        case "LAUTARO":
            alert("HOLA LAUTARO");
            break;
        default:
            alert("QUIEN SOS??");
            break;
    }
    nombre_ingresado = prompt("Ingrese un nombre");
}
let edad = prompt("Ingrese su edad")
if (edad == undefined){
    alert("Lo siento debo saver tu edad")
}else if(parseInt(edad) >= 18){
    alert("Puede Ingresar")
}
alert(typeof true) // dice el tipo de dato

let confirmar_turno = confirm("Bienvenido a la peluqueria tiene turno?")

if (confirmar_turno == true){
    let nombre_de_usuario = prompt("Ingrese su nombre");
}
else {
    alert("Solo atendemos con turno previo")
}