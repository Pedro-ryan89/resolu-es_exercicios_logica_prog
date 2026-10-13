from socket import *

nome_servidor = "localhost"
porta_servidor = 12000
porta_receptor = 12001

socket_receptor = socket(AF_INET, SOCK_DGRAM)
socket_receptor.bind(("", porta_receptor))

socket_receptor.sendto(
    "!REGISTRO_RECEPTOR".encode(),
    (nome_servidor, porta_servidor)
)

while True:
    mensagem, endereco_servidor = socket_receptor.recvfrom(2048)
    print(mensagem.decode())