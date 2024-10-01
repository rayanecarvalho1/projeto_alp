assentos = {}
for fileira in range(1, 31):
    for coluna in ['A', 'B', 'C', 'D', 'E', 'F']:
        assentos[f'{coluna}{fileira}'] = None


def marcar_assento(assento, classe):
    if assento in assentos and assentos[assento] is None:
        assentos[assento] = {"classe": classe}
        print(f"Assento {assento} marcado com sucesso.")
    else:
        print(f"O assento {assento} já está ocupado ou não existe.")


def desmarcar_assento(assento):
    if assento in assentos and assentos[assento] is not None:
        assentos[assento] = None
        print(f"Assento {assento} desmarcado com sucesso.")
    else:
        print(f"O assento {assento} já está vazio ou não existe.")


def remarcar_assento(assento_atual, novo_assento, classe):
    desmarcar_assento(assento_atual)
    marcar_assento(novo_assento, classe)


def imprimir_relatorio():
    ocupados = sum(1 for a in assentos if assentos[a] is not None)
    vazios = len(assentos) - ocupados
    primeira_classe = sum(
        1 for a in assentos
        if assentos[a] is not None and assentos[a]["classe"] == "executiva")
    classe_normal = ocupados - primeira_classe
    total_pago_executiva = primeira_classe * 100
    total_pago_normal = classe_normal * 80
    total_pago_geral = total_pago_executiva + total_pago_normal

    print(f"Quantidade de assentos ocupados: {ocupados}")
    print(f"Quantidade de assentos vazios: {vazios}")
    print("Assentos ocupados:")
    for assento, info in assentos.items():
        if info is not None:
            print(f"{assento}: {info['classe']}")
    print(f"Assentos ocupados na primeira classe: {primeira_classe}")
    print(f"Assentos ocupados na classe normal: {classe_normal}")
    print(f"Total pago por todos os passageiros: R${total_pago_geral:.2f}")
    print(
        f"Total pago por passageiros da classe executiva: R${total_pago_executiva:.2f}"
    )
    print(
        f"Total pago por passageiros da classe normal: R${total_pago_normal:.2f}"
    )


def marcar_varios_assentos():
    while True:
        print("Digite 'parar' para encerrar.")
        assento = input("Informe o assento para marcar: ").upper()
        if assento == "PARAR":
            break
        fileira = int(assento[1:])
        if 1 <= fileira <= 6:
            classe = "executiva"
        else:
            classe = "normal"
        marcar_assento(assento, classe)


def menu():
    marcar_varios_assentos()
    while True:
        print("----- Menu -----")
        print("1. Marcar assento")
        print("2. Desmarcar assento")
        print("3. Remarcar assento")
        print("4. Imprimir relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            assento = input("Informe o assento para marcar: ").upper()
            fileira = int(assento[1:])
            if 1 <= fileira <= 6:
                classe = "executiva"
            else:
                classe = "normal"
            marcar_assento(assento, classe)

        elif opcao == "2":
            assento = input("Informe o assento para desmarcar: ").upper()
            desmarcar_assento(assento)

        elif opcao == "3":
            assento_atual = input(
                "Informe o assento atual para remarcar: ").upper()
            novo_assento = input(
                "Informe o novo assento para remarcar: ").upper()
            if assentos[assento_atual] is not None:
                fileira = int(novo_assento[1:])
                if 1 <= fileira <= 6:
                    classe = "executiva"
                else:
                    classe = "normal"
                remarcar_assento(assento_atual, novo_assento, classe)
            else:
                print("Assento atual não está ocupado.")

        elif opcao == "4":
            imprimir_relatorio()

        elif opcao == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
