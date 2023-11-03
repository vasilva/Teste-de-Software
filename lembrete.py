from datetime import datetime as dt
from calendario import *

def main():

    calendario = Calendario()

    while True:
        print("\n===== Calendário =====")
        print("1. Adicionar evento")
        print("2. Visualizar eventos")
        print("3. Remover evento")
        print("4. Sair")

        choice = input("Escolha uma opção: ")
        if choice == "1":
            date_str = input("Escolha uma data (AAAA-MM-DD): ")
            evento = input("Escolha o evento: ")
            data = dt.strptime(date_str, "%Y-%m-%d")
                    
        elif choice == "2":
            ano = int(input("Digite o ano: "))
            mes = int(input("Digite o mês: "))
            
        elif choice == "3":
            break
        
        elif choice == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
