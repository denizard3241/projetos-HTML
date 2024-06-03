<?php
// Conexão com o banco de dados (supondo que estamos usando MySQL)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "minhabase";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica a conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Recebe os dados do formulário
$username = $_POST['username'];
$password = $_POST['password'];

// Consulta SQL vulnerável à injeção
$sql = "SELECT * FROM usuarios WHERE username='$username' AND password='$password'";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Usuário autenticado
    echo "Login bem-sucedido!";
} else {
    // Login falhou
    echo "Nome de usuário ou senha incorretos!";
}

$conn->close();
?>
