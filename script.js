document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Impede o envio do formulário

  var username = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (username === "" || password === "") {
    alert("Por favor, preencha todos os campos!");
    return;
  }

  // Aqui você pode adicionar a lógica para enviar os dados para o backend e realizar a autenticação


  // Exemplo de envio dos dados para o backend usando o Fetch API
  function openRegisterPage() {
  window.location.href = "http://localhost:5000/cadastro";
}
