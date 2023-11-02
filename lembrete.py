import calendar
import matplotlib.pyplot as plt

calendar.setfirstweekday(6)  # Domingo como 1o dia
nomes_dias = "Dom Seg Ter Qua Qui Sex Sab".split()
nomes_meses = """ 
                Janeiro Fevereiro Março
                Abril Maio Junho
                Julho Agosto Setembro
                Outubro Novembro Dezembro""".split()


class Calendario(object):
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes
        self.cal = calendar.monthcalendar(ano, mes)
        self.eventos = [[[] for dia in semana] for semana in self.cal]

    def _dia_do_mes_to_index(self, dia):
        for n_semana, semana in enumerate(self.cal):
            try:
                i = semana.index(dia)
                return n_semana, i
            except ValueError:
                pass

        raise ValueError("Não há {} dias no mês".format(dia))

    def add_evento(self, dia, evento_str):
        semana, nomes_dias = self._dia_do_mes_to_index(dia)
        self.eventos[semana][nomes_dias].append(evento_str)

    def get_evento(self, dia):
        semana, dia_semana = self._dia_do_mes_to_index(dia)
        return self.eventos[semana][dia_semana]

    def show(self):
        f, axs = plt.subplots(len(self.cal), 7, sharex=True, sharey=True)
        for semana, ax_row in enumerate(axs):
            for dia_semana, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[semana][dia_semana] != 0:
                    ax.text(
                        0.02,
                        0.98,
                        str(self.cal[semana][dia_semana]),
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
            axs[0][n].set_title(dia)

        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(
            nomes_meses[self.mes - 1] + " " + str(self.ano),
            fontsize=20,
            fontweight="bold",
        )
        plt.show()


def main():
    feb = Calendario(2023, 2)
    feb.add_evento(1, "1o dia de Fevereiro")
    feb.add_evento(2, "Evento 1")
    feb.add_evento(2, "Evento 2")
    print(feb.get_evento(1))


if __name__ == "__main__":
    main()
