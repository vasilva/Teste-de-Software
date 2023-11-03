from mes import Mes


class Calendario:
    def __init__(self):
        self.anos = {}
    
    def add_ano(self, ano):
        if ano not in self.anos:
            self.anos[ano] = Ano(ano)


# Um calendario de um ano
class Ano(object):
    def __init__(self, ano):
        # Cria os 12 meses de um ano
        self.calendario = [Mes(ano, mes) for mes in range(1, 13)]
        self.ano = ano
        self.count = 0

    def add_evento(self, dia, mes, evento_str):
        self.calendario[mes - 1].add_evento(dia, evento_str)
        self.count += 1

    def remove_evento(self, dia, mes):
        count = self.calendario[mes - 1].remove_eventos(dia)
        self.count -= count

    def clear_eventos(self):
        for mes in self.calendario:
            mes.clear_eventos()
        self.count = 0

    def get_evento(self, dia, mes):
        return self.calendario[mes - 1].get_evento(dia)

    def get_mes(self, mes):
        return self.calendario[mes - 1]

    def show(self, mes=1):
        self.calendario[mes - 1].show()
