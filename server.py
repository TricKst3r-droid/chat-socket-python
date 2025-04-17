import socket
import threading

clientes = []


def broadcast(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.send(mensagem)
            except:
                clientes.remove(cliente)


def tratar_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            print("Mensagem recebida:", mensagem.decode())
            broadcast(mensagem, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break


# Criar socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 12345))
servidor.listen()

print("Servidor está escutando na porta 12345...")

while True:
    cliente, endereco = servidor.accept()
    print(f"Conectado a {endereco}")
    clientes.append(cliente)
    thread = threading.Thread(target=tratar_cliente, args=(cliente,))
    thread.start()
