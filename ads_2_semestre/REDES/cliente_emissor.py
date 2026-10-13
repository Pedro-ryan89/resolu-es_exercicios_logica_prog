from socket import *

nome_servidor = "localhost"
porta_servidor = 12000

socket_cliente = socket(AF_INET, SOCK_DGRAM)

socket_cliente.sendto(
    "!REGISTRO".encode(),
    (nome_servidor, porta_servidor)
)

nome_cliente = input("digite seu nickname: ")

while True:
    mensagem = input("Digite algo: ")
    mensagem_cliente = f"{nome_cliente}: {mensagem}"
    print(f"{nome_cliente}: {socket_cliente.sendto(mensagem_cliente.encode(),(nome_servidor, porta_servidor))}")