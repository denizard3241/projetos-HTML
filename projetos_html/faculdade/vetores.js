var numeros = [];

numeros[0] = solicitarPrimeiroNumero();
numeros[1] = solicitarSegundoNumero();

var resultadoDivisao = divida(numeros);
alert('o resultado da divisão é igual a :' + resultadoDivisao);

    function solicitarPrimeiroNumero(){
        var numero1 = prompt("Insira o Primeiro Número aqui :");
        if(numero1 <= 0) {
            alert("o numero precisa ser inteiro e positivo");
            return solicitarPrimeiroNumero();
        }   else {
            return numero1;
        }
     }

     function solicitarSegundoNumero()  {
        var numero2 = prompt("Insira o segundo:");
        if(numero2 <= 0) {
            alert("digite um valor maior que zero")
            return solicitarSegundoNumero();

        } else {
            return numero2;
        }
    }

    function divida(numeros){
        var resultado = 0;
        

        resultado = numeros[0] / numeros[1];
        return resultado;

    }