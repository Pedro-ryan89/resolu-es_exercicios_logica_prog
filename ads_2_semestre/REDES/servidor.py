from socket import *

porta_servidor = 12000
socket_servidor = socket(AF_INET, SOCK_DGRAM)
endereco_receptor = None

socket_servidor.bind(("", porta_servidor))

print("Servidor pronto para receber")

cliente_registrado = None

while True:
    mensagem, endereco_cliente = socket_servidor.recvfrom(2048)
    mensagem = mensagem.decode()

    if mensagem == "!REGISTRO":
        cliente_registrado = endereco_cliente
        print("Cliente registrado:", cliente_registrado)

    elif mensagem == "!REGISTRO_RECEPTOR":
        endereco_receptor = endereco_cliente
        print("Receptor registrado:", endereco_receptor)

    else:
        if endereco_receptor is not None:
            socket_servidor.sendto(mensagem.encode(),endereco_receptor)