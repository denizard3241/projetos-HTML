const XLSX = require('xlsx');

// Função para coletar os dados das pessoas a partir de argumentos da linha de comando
function coletarDados(args) {
    const data = [];
    
    for (let i = 2; i < args.length; i += 3) {
        const nome = args[i];
        const idade = parseInt(args[i + 1]);
        const pais = args[i + 2];

        if (!isNaN(idade)) {
            data.push([nome, idade, pais]);
        } else {
            console.error(`Erro: Idade inválida para ${nome}`);
        }
    }

    return data;
}

// Verificar se foram passados argumentos da linha de comando
if (process.argv.length < 3 || (process.argv.length - 2) % 3 !== 0) {
    console.error('Uso: node criar_planilha.js <nome1> <idade1> <país1> <nome2> <idade2> <país2> ...');
    process.exit(1);
}

// Criar uma nova planilha
const workbook = XLSX.utils.book_new();
const worksheet = XLSX.utils.aoa_to_sheet(coletarDados(process.argv));

// Adicionar a planilha ao arquivo
XLSX.utils.book_append_sheet(workbook, worksheet, 'Pessoas');

// Salvar a planilha em um arquivo
const excelFileName = 'pessoas.xlsx';
XLSX.writeFile(workbook, excelFileName);

console.log(`Planilha criada: ${excelFileName}`);
