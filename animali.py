class Animali:
    
    nome = ''

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "nome: " + self.nome
    
    def emettiVerso(self):
        return "NON SO PARLARE"


class Mammuth(Animali):
    def emettiVerso(self):
        return "BARRITO"

    def zanne(self):
        return "ho le zanne"

class Cocorita(Animali):
    def emettiVerso(self):
        return "CHIPPO"

    def zanne(self):
        return "NON ho le zanne"
    