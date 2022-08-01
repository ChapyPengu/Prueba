let productos_terminados = ['Medialunas de manteca','Medialunas de grasa','Cremonas de grasa','Donas con dulce',
'alfajores con dulce','fastaflora con membrillo','Surtidas de manteca','Surtidas de grasa']

let materias_primas = ['Harina','Manteca','Azucar','Maicena','Huevo','Dulce de leche',
'Azucar impalpable','Pulpa','Membrillo','Margarina']

const precio = 60
let total = 0
let eleccion_productos = []
let eleccion = false
while (true){
    let motivos = promt("Buenas digame...Productos terminados o Materia prima");
    if (motivos == "Productos terminados"){
        eleccion = true
        break;
    }else if (motivos == "Materias primas"){
        eleccion = false
        break;
    }else{
        alert("Perdon...Solo entiendo: .Productos terminados o .Materias primas");
    }
}
alert("si desea terminar la compras ponga salir o exit")
while (true){
    if (eleccion == false){
        let producto = prompt(materias_primas + "ingrese el producto");
        eleccion_productos.push(producto)
        if (producto == "salir " || producto == "exit"){
            break;
        }
    }else{
        let producto = promt(productos_terminados + "ingrese el producto");
        eleccion_productos.push(producto)
        if (producto == "salir " || producto == "exit"){
            break;
        }
    }

    total = total + precio
}
alert("Total a abonar:" + total + "sus productos son:" + eleccion_productos)