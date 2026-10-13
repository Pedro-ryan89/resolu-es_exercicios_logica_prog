from socket import *

nome_servidor = "localhost"
porta_servidor = 12000
socket_cliente = socket(AF_INET, SOCK_DGRAM)



while True:
    mensagem = input("Digite algo (em caixa baixa): ")
    socket_cliente.sendto(mensagem.encode(), (nome_servidor, porta_servidor))

    resposta, endereco_servidor = socket_cliente.recvfrom(2048)
    print("Resposta do servidor: ", resposta.decode())

socket_cliente.close()