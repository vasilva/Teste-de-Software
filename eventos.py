from datetime import datetime as dt
from calendario import *


def print_opcoes():
    print("\n===== Calendário =====")
    print("1. Adicionar evento")
    print("2. Visualizar evento")
    print("3. Visualizar todos eventos")
    print("4. Visualizar mês")
    print("5. Remover evento")
    print("6. Remover todos eventos")
    print("7. Sair")


def get_data():
    date_str = input("Escolha uma data (AAAA-MM-DD): ")
    return dt.strptime(date_str, "%Y-%m-%d")


def main():
    calendario = Calendario()

    while True:
        print_opcoes()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            data = get_data()
            evento = input("Escolha o evento: ")
            calendario.add_ano(data.year)
            calendario.anos[data.year].add_evento(data.day, data.month, evento)
            print("Evento adicionado com sucesso!")

        elif choice == "2":
            data = get_data()
            m = calendario.anos[data.year].get_mes(data.month)
            m.print_eventos(data.day)

        elif choice == "3":
            for ano in calendario.anos.values():
                for mes in ano.calendario:
                    mes.print_eventos()

        elif choice == "4":
            data = get_data()
            calendario.anos[data.year].show(data.month)

        elif choice == "5":
            data = get_data()
            calendario.anos[data.year].get_mes(data.month).remove_eventos(data.day)
            print("Eventos em", data.date(), "removidos!")

        elif choice == "6":
            for ano in calendario.anos.values():
                for mes in ano.calendario:
                    mes.clear_eventos()
            print("Todos eventos removidos!")

        elif choice == "7":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
