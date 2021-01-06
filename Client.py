import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) # kiedy się łączymy wysyłana jest jakaś wiadomość od klienta dlatego potrzebujemy ifa w serwerze


def send(msg):
    message = msg.encode(FORMAT) # musimy je zakodować w obiekt składający się z bajtów
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # kodujemy długość jako string
    send_length += b' ' * (HEADER - len(send_length))
    client.sendall(send_length)
    client.sendall(msg.encode(FORMAT))
    print(client.recv(2048).decode(FORMAT))

send(input())
send(input())
send(input())
send(input())
send(input())

