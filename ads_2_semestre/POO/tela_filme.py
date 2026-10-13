from sitema_filme import Filme
from sitema_filme import Catalogo

import os


catalogo = Catalogo()


while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("\n===== CONTROLE DO FILME =====")
    print("1 - Adicionar filme")
    print("2 - Remover filme")
    print("3 - Listar filmes")
    print("4 - Sair")

    print("\n===== INFORMAÇÕES =====")

    opcao = input("\nEscolha uma opção: ")

    match opcao:

        case "1":
            try:
                titulo = input("Título: ")
                diretor = input("Diretor: ")
                ano = int(input("Ano: "))
                genero = input("Gênero: ")

                filme = Filme(titulo, diretor, ano, genero)
                catalogo.adicionar_filme(filme)

                print("Filme adicionado com sucesso!")

            except (ValueError, TypeError) as erro:
                print(f"Erro: {erro}")

        case "2":
            try:
                titulo = input("Digite o título do filme: ")

                catalogo.remover_filme(titulo)

                print("Filme removido com sucesso!")

            except ValueError as erro:
                print(f"Erro: {erro}")

        case "3":
            try:
                genero = input("Digite o gênero: ")

                catalogo.listar_filme(genero)

            except ValueError as erro:
                print(f"Erro: {erro}")

        case "4":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")

    input("\nPressione ENTER para continuar...")
