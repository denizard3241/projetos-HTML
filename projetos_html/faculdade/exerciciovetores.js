function realizarDivisao() {
    let numero1 = parseInt(document.getElementById("numero1").value);
    let numero2 = parseInt(document.getElementById("numero2").value);
    let numero3 = parseInt(document.getElementById("numero3").value);
    let numero4 = parseInt(document.getElementById("numero4").value);
    let resultadoDivisao = document.getElementById("resultado");

    if (isNaN(numero1) || isNaN(numero2) || isNaN(numero3) || isNaN(numero4) || numero1 <= 0 || numero2 <= 0 || numero3 <= 0 || numero4 <= 0) {
        resultadoDivisao.textContent = "Por favor, insira apenas números inteiros positivos.";
    } else {
        if (numero2 === 0 || numero4 === 0) {
            resultadoDivisao.textContent = "Impossível dividir por zero.";
        } else {
            let resultado = (numero1 + numero2 + numero3 + numero4) / 4;
            resultadoDivisao.textContent = "A média dos números é: " + resultado;
        }
    }
}
