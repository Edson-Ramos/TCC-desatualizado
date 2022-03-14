
class Equipamento:

    def __init__(self, id, nome, linha, trecho):
        self.id = id
        self.nome = nome
        self.linha = linha
        self.trecho = trecho


    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
		

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getLinha(self):
        return self.linha
    def setLinha(self, linha):
        self.linha = linha

    def getTrecho(self):
        return self.trecho
    def setTrecho(self, trecho):
        self.trecho = trecho
