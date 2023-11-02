import calendar
import matplotlib.pyplot as plt

calendar.setfirstweekday(6)  # Domingo como 1o dia
# Nomes dos dias da semana
nomes_dias = "Domingo Segunda Terça Quarta Quinta Sexta Sábado".split()

# Nomes dos 12 meses
nomes_meses = """ 
                Janeiro Fevereiro Março
                Abril Maio Junho
                Julho Agosto Setembro
                Outubro Novembro Dezembro""".split()


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


# Um calendario de um mes
class Mes(object):
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes
        self.calendario = calendar.monthcalendar(ano, mes)
        # Uma lista de eventos para cada dia
        self.eventos = [[[] for dia in semana] for semana in self.calendario]
        self.count = 0

    # Encontra o dia da semana de um dia
    def _dia_do_mes_to_index(self, dia):
        for n_semana, semana in enumerate(self.calendario):
            try:
                i = semana.index(dia)
                return n_semana, i
            except ValueError:
                pass

        # Caso o valor do dia seja inválido
        raise ValueError("Não há {} dias no mês".format(dia))

    def add_evento(self, dia, evento_str):
        semana, nomes_dias = self._dia_do_mes_to_index(dia)
        self.eventos[semana][nomes_dias].append(evento_str)
        self.count += 1

    def get_evento(self, dia):
        semana, dia_semana = self._dia_do_mes_to_index(dia)
        return self.eventos[semana][dia_semana]

    def remove_eventos(self, dia):
        semana, dia_semana = self._dia_do_mes_to_index(dia)
        dia_evento = self.eventos[semana][dia_semana]
        n_eventos = len(dia_evento)
        if len(dia_evento) > 0:
            dia_evento.clear()
            self.count -= n_eventos
        return n_eventos

    def clear_eventos(self):
        semana, dias = calendar.monthrange(self.ano, self.mes)
        for i in range(1, dias + 1):
            self.remove_eventos(i)

    def print_eventos(self, dia=None):
        print("Mês {} contém".format(nomes_meses[self.mes - 1]), self.count, "eventos")
        if self.count > 0:
            print("Lista de Eventos:")
            if dia != None:
                eventos = self.get_evento(dia)
                print("Dia:", dia)
                for evento in eventos:
                    print("  " + evento)

            else:
                semana, dias = calendar.monthrange(self.ano, self.mes)
                for i in range(1, dias + 1):
                    eventos = self.get_evento(i)
                    if eventos != []:
                        print("Dia:", i)
                        for evento in eventos:
                            print("  " + evento)

    def show(self):
        f, axs = plt.subplots(len(self.calendario), 7, sharex=True, sharey=True)
        for semana, ax_row in enumerate(axs):
            for dia_semana, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.calendario[semana][dia_semana] != 0:
                    ax.text(
                        0.02,
                        0.98,
                        str(self.calendario[semana][dia_semana]),
                        verticalalignment="top",
                        horizontalalignment="left",
                    )
                    contents = "\n".join(self.eventos[semana][dia_semana])
                    ax.text(
                        0.03,
                        0.85,
                        contents,
                        verticalalignment="top",
                        horizontalalignment="left",
                        fontsize=9,
                    )
        for n, dia in enumerate(nomes_dias):
            axs[0][n].set_title(dia[:1])

        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(
            nomes_meses[self.mes - 1] + " " + str(self.ano),
            fontsize=20,
            fontweight="bold",
        )
        plt.show()
