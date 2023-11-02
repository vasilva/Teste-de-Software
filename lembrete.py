from calendario import *

def main():
    ano = Ano(2024)
    feb = ano.get_mes(2)
    feb.add_evento(1, "1o dia de Fevereiro")
    feb.add_evento(2, "Evento 1")
    feb.add_evento(2, "Evento 2")
    feb.print_eventos()
    feb.clear_eventos()
    feb.show()
    feb.print_eventos()

if __name__ == "__main__":
    main()
