from ads_2_semestre.POO.PedroRyanCoelhoDoNascimento_prova_poo_arq01 import Drone
import os

drone = Drone()



while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("\n===== CONTROLE DO DRONE =====")
    print("1 - Voar")
    print("2 - Mover")
    print("3 - Sair")

    print("\n===== INFORMAÇÕES =====")
    print(drone)

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            try:
                deslocamento_z = int(
                    input("Informe o deslocamento vertical: ")
                )
                drone.voar(deslocamento_z)

            except (TypeError, ValueError) as error:
                print(f"Erro: {error}")

        case "2":
            try:
                deslocamento_x = int(
                    input("Informe o deslocamento no eixo X: ")
                )

                deslocamento_y = int(
                    input("Informe o deslocamento no eixo Y: ")
                )

                drone.mover(deslocamento_x, deslocamento_y)

            except (TypeError, ValueError, RuntimeError) as error:
                print(f"Erro: {error}")

        case "3":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")