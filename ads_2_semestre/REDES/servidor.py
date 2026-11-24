from socket import *

porta_servidor = 12000
socket_servidor = socket(AF_INET, SOCK_STREAM)
socket_servidor.bind( ("",porta_servidor) )
socket_servidor.listen(1)

print(f"Servidor ouvindo porta {porta_servidor}")

while True:
    socket_conexao, endereco_cliente = socket_servidor.accept()

    print(f"Solicitação de conexão recebida de {endereco_cliente}")

    mensagem = socket_conexao.recv(1024).decode()
    resposta = mensagem.upper()
    socket_conexao.send( resposta.encode() )
    socket_conexao.close()
