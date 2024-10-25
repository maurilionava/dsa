const a = [1,2,2,4,4]
const b = [2,2,3,4,5]
const k = 2
let controleK = 0
let valorAnterior = 0
let arrayPadronizado = []
let aux = 0

console.log(`a antes das trocas=${a}`)
console.log(`b antes das trocas=${b}`)

const existeValorNoArray = (valor, array) => {
    for(let i=0; i<array.length;i++){
        if(array[i] === valor){
            return true
        }
    }

    return false;
}

//percorrer o array principal
for(let i=0; i<a.length;i++){
    a[i] //valor atual

    //encontrar valores repetidos em sequencia
    if(valorAnterior === a[i] && controleK < k){
        //buscar valor distinto para troca
        //percorrer o array reserva
        for(let j=0; j<b.length;j++){
            //busco valor distinto dos existentes no array padronizado
            //caso valor seja diferente do repetido e não exista no array padronizado deve ser inserido no array padronizado
            if(b[j] !== a[i] && !existeValorNoArray(b[j], arrayPadronizado)){
                //se houver a troca de valores, deve quebrar a execução de demais loops
                aux = b[j]
                b[j] = a[i]
                a[i] = aux
                aux = 0
                controleK += 1
                arrayPadronizado.push(a[i])
                break;
            }
        }
    } else {
        arrayPadronizado.push(a[i])
    }

    valorAnterior = a[i] //anterior
}

console.log(`a após trocas=${a}`)
console.log(`b após trocas=${b}`)
console.log(`array padronizado=${arrayPadronizado}`)