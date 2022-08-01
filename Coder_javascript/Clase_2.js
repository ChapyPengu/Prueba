console.log("HOLA QUE HACE")//console.log muestra un mensaje por consola.
alert("ANASHEI")// alert es una funcion que nos genera una alerta en la pagina web.

// Si -- Condicion --
if (true){
    // Bloque de codigo a ejecutar
    alert("ES TRUE!") 
    console.log("Vas a ver este mensaje");


}
if (false){
    // Condidcion false -- El bloque no se ejecutara
    alert("Es true!!")
}


let num = 1000

if (num > 150){ // SI LA CONDICION DEVUELVE TRUE SE EJECUTARA EL SIGUENTE BLOQUE
    alert("El numero es mayor a 150")
}
else{ // SINO..
    alert("El numero es menor a 150")
}

let dato = true
console.log(dato)
dato = false

// Bar > 18 para ingresar

let edad = prompt("Ingrese su edad") // funcion prompt, Pide mediante una alerta datos ingresados por el usuario. similar a input.
puede_ingresar = false
if(edad >= 18){
    console.log("Es mayor de edad")
    puede_ingresar = true
}
else{
    console.log("Es menor de edad")
    puede_ingresar = false
}
if(edad >= 18){
    console.log("Puede ingresar")
}
else if (edad < 18){
    console.log("No puede ingresar")
}
else if (edad == 18){
    console.log("Tiene 18, puede ingresar")
}
else{
    alert("Tiene 18, puede ingresar")
}

let a = 50
console.log(a + 10)

a = parseString(a)
a = parseInt(a)
a = parseFloat(a) // parseInt es una funcion de convercion similar a Int en python
console.log(a + 10)

// AND &&

// COLOR = BLANCO AND BOTONES == true -> Control del aire

// OR ||

let nombre_ingresado = prompt("Ingresar su nombre")
let apeliido_ingresado = prompt("Ingrese su apellido")

if ((nombre_ingresado != "") && (apeliido_ingresado != "")){
    alert("Nombre: "+nombre_ingresado +"\nApellido: "+apeliido_ingresado)
}else{
    alert("ERROR")
}
