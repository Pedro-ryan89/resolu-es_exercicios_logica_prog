from socket import *

nome_servidor = "macavi.com.br"
porta_servidor = 80

socket_cliente = socket(AF_INET, SOCK_STREAM)
socket_cliente.connect((nome_servidor, porta_servidor))

mensagem = (
    "GET / HTTP/1.1\r\n"
    "Host: macavi.com.br\r\n"
    "Connection: close\r\n"
    "\r\n"
)

socket_cliente.sendall(mensagem.encode())

while True:
    resposta = socket_cliente.recv(1024)

    if not resposta:
        break

    print(resposta.decode("utf-8", errors="replace"), end="")

socket_cliente.close()