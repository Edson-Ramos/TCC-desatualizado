const rota = 'http://localhost:5000'

function getArquivos(){
    
    fetch(`${rota}/listar`)
    .then(data => {        
        return data.json();
    })
.then(data => {    
    for(file of data.files)        
        createFile(file);
    
    })
}

var ul = document.getElementById("ul")
let divElement = document.createElement("div")
divElement.className = "container"

function createFile(file){
   
    let hr = document.createElement("hr")
    // Criando a Div e as li(linha)
    let liIdElement = document.createElement("li")
    let brId = document.createElement("br")
    liIdElement.className = "list-group-item active"
    liIdElement.innerText = `Id: ${file.id}`
    

    let liNomeElement = document.createElement("li")
    let brSn = document.createElement("br")
    liNomeElement.className = "list-group-item"
    liNomeElement.innerText = `Nome : ${file.nome}`

    let liSNomeElement = document.createElement("li")
    let brN = document.createElement("br")
    liSNomeElement.className = "list-group-item"
    liSNomeElement.innerText = `Sobre Nome: ${file.sobreNome}`

    let liEmailElement = document.createElement("li")
    let brE = document.createElement("br")
    liEmailElement.className = "list-group-item"
    liEmailElement.innerText = `Email: ${file.email}`

    let liSenhaElement = document.createElement("li")
    let brS = document.createElement("br")
    liSenhaElement.className = "list-group-item"
    liSenhaElement.innerText = `Senha: ${file.senha}` 
    
   ul.appendChild(divElement)
   divElement.appendChild(liIdElement)
   divElement.appendChild(brId)
   divElement.appendChild(liNomeElement)
   divElement.appendChild(brN)
   divElement.appendChild(liSNomeElement)
   divElement.appendChild(brSn)
   divElement.appendChild(liEmailElement)
   divElement.appendChild(brE)
   divElement.appendChild(liSenhaElement)
   divElement.appendChild(brS)
   divElement.appendChild(hr)
   
}
