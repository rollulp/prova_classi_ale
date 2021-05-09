class Cane:

    nome = ""
    eta = 0
    colore = ""

    def __init__(self, nome, eta, colore="???"):
        self.nome = nome
        self.eta = eta
        self.colore = colore
    
    def __str__(self):
        return "nome: " + self.nome + "  eta: " + str(self.eta) + "   colore: " + self.colore