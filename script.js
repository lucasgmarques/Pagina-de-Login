document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Impede o envio do formulário

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username === "" || password === "") {
    alert("Por favor, preencha todos os campos!");
    return;
  }

  // Aqui você pode adicionar a lógica para enviar os dados para o backend e realizar a autenticação

  // Exemplo de envio dos dados para o backend usando o Fetch API
  fetch("/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      username: username,
      password: password
    })
  })
  .then(response => response.json())
  .then(data => {
    // Aqui você pode tratar a resposta do backend, como exibir uma mensagem de sucesso ou erro
    console.log(data);
  })
  .catch(error => {
    // Tratar erros de requisição ou resposta do backend
    console.error(error);
  });
});
