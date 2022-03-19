

function cadastrar_usuario() {
    let idServico = document.getElementById("idServico").value;
    let maquina = document.getElementById("maquina").value;
    let linhaMaq = document.getElementById("linhaMaq").value;
    let trecho = document.getElementById("trechoMaq").value
    let tipLub = document.getElementById("tipLub").value;
    let dataAplic = document.getElementById("dataAplic").value
    let obs = document.getElementById("obs").value

    let dados_servico = {
        idServico: idServico,
        maquina: maquina,
        linhaMaq: linhaMaq,
        trecho: trecho,
        tipLub: tipLub,
        dataAplic: dataAplic,
        obs: obs
    }
    if (idServico == "" || maquina == "" || linhaMaq == "" || trecho == "" || tipLub == "" || dataAplic == "" || obs == ""){
        return alert("Todos os campos são obrigatorios!")
    } else {
            fetch("/cadastro_servico",
                {
                    method: "POST",
                    body: JSON.stringify(dados_servico),
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
                .then((resposta) => {
                    if (resposta.status == 200)
                        return resposta.text()
                    else
                        return "Erro ao cadastrar serviço"
                })
                .then((repostaTexto) => {
                    alert(repostaTexto)
                    document.location.reload(true);
                })
    }

}
