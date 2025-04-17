import socket
import threading


def receber_mensagens(sock):
    while True:
        try:
            mensagem = sock.recv(1024).decode()
            print("Servidor:", mensagem)
        except:
            print("Conexão encerrada.")
            break


# Criar socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345))

print("Conectado ao servidor. Você pode digitar as mensagens:")

# Thread para receber mensagens
thread = threading.Thread(target=receber_mensagens, args=(cliente,))
thread.start()

# Enviar mensagens
while True:
    msg = input()
    cliente.send(msg.encode())
