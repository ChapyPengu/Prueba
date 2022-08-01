// Funciones
function calculadora(primerNumero, segundoNumero, operacion) {
    switch (operacion) {
        case "+":
            return primerNumero + segundoNumero
            break;
        case "-":
            return primerNumero - segundoNumero
            break;
        case "/":
            return primerNumero / segundoNumero
            break;
        case "*":
            return primerNumero * segundoNumero
            break;
        default:
            return 0;
            break;
    }
}
console.log(calculadora(8, 2, "/"));

const suma = (a,b) => a + b
const resta = (a,b) => a - b
// Si una funcion es una sola linea con retorno y un parametro
// puede evitar escribir los ()

const iva = x => x * 0.21
let precioProducto = 500
let descuento = 50
// Calculo el precioProducto + IVA - descuento
let nuevoPrecio = resta(suma(precioProducto, iva(precioProducto), descuento));
console.log(nuevoPrecio);

