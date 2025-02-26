# amigo-secreto-
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amigo Secreto</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        input, button { margin: 5px; padding: 10px; }
        #resultado { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Sorteio de Amigo Secreto</h2>
    <input type="text" id="nome" placeholder="Digite um nome">
    <button onclick="adicionarNome()">Adicionar Nome</button>
    <button onclick="sortear()">Sortear</button>
    <ul id="lista"></ul>
    <div id="resultado"></div>

    <script>
        let nomes = [];

        function adicionarNome() {
            let nome = document.getElementById("nome").value.trim();
            if (nome && !nomes.includes(nome)) {
                nomes.push(nome);
                document.getElementById("lista").innerHTML += `<li>${nome}</li>`;
                document.getElementById("nome").value = "";
            }
        }

        function sortear() {
            if (nomes.length < 2) {
                alert("Adicione pelo menos 2 nomes para sortear!");
                return;
            }
            let sorteio = {};
            let sorteados = [...nomes];
            let embaralhado = [...nomes].sort(() => Math.random() - 0.5);
            
            for (let i = 0; i < nomes.length; i++) {
                if (nomes[i] === embaralhado[i]) {
                    embaralhado = [...nomes].sort(() => Math.random() - 0.5);
                    i = -1;
                }
            }

            for (let i = 0; i < nomes.length; i++) {
                sorteio[nomes[i]] = embaralhado[i];
            }
            
            let resultado = "<h3>Resultado do Sorteio:</h3>";
            for (let chave in sorteio) {
                resultado += `<p>${chave} --> ${sorteio[chave]}</p>`;
            }
            document.getElementById("resultado").innerHTML = resultado;
        }
    </script>
</body>
</html>
