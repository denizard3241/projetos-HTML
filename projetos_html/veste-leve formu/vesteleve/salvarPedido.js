// Importar a biblioteca docxtemplater
const { Docxtemplater } = require('docxtemplater');

function salvarPedido() {
    // Obter os valores do formulário
    var modelo = document.getElementById('modelo').value;
    var tamanho = document.getElementById('tamanho').value;
    var quantidade = document.getElementById('quantidade').value;
    var referencia = document.getElementById('referencia').value;
    var preco = document.getElementById('preco').value;

    // Criar um objeto com os dados do pedido
    var pedido = {
        modelo: modelo,
        tamanho: tamanho,
        quantidade: quantidade,
        referencia: referencia,
        preco: preco
    };

    // Carregar o conteúdo do modelo do documento Word
    var templateContent = fs.readFileSync('caminho/do/seu/modelo.docx', 'binary');

    // Criar um objeto docxtemplater com o conteúdo do modelo
    var doc = new Docxtemplater();
    doc.loadZip(new JSZip(templateContent));

    // Substituir as variáveis no modelo pelos dados do pedido
    doc.setData({
        modelo: pedido.modelo,
        tamanho: pedido.tamanho,
        quantidade: pedido.quantidade,
        referencia: pedido.referencia,
        preco: pedido.preco
    });

    // Renderizar o documento
    doc.render();

    // Obter o conteúdo renderizado do documento
    var documentoWord = doc.getZip().generate({ type: 'nodebuffer' });

    // Criar um objeto Blob com o conteúdo do documento Word
    var blob = new Blob([documentoWord], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });

    // Criar um link para fazer o download do arquivo
    var link = document.createElement('a');
    link.download = 'pedido.docx';
    link.href = window.URL.createObjectURL(blob);
    link.click();
}
