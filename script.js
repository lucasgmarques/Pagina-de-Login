document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Impede o envio do formulário

  var username = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (username === "" || password === "") {
    alert("Por favor, preencha todos os campos!");
    return;
  }

  // Aqui você pode adicionar a lógica para enviar os dados para o backend e realizar a autenticação

  // Criar um objeto com os dados do formulário
  var formData = {
    email: username,
    password: password
  };

  // Enviar os dados para o servidor usando a Fetch API
  fetch("/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
  })
  .then(function(response) {
    if (response.ok) {
      // Sucesso - exibir a resposta do servidor
      return response.text();
    } else {
      // Erro - lançar uma exceção para ser capturada no bloco catch
      throw new Error("Ocorreu um erro durante a autenticação. Por favor, tente novamente.");
    }
  })
  .then(function(data) {
    // Exibir a resposta do servidor
    alert(data);
    // Redirecionar para uma nova página, se necessário
    // window.location.href = "/dashboard";
  })
  .catch(function(error) {
    // Capturar e exibir o erro
    alert(error.message);
  });
});

  // Exemplo de envio dos dados para o backend usando o Fetch API
  function openRegisterPage() {
  window.location.href = "http://localhost:5000/cadastro";
}
