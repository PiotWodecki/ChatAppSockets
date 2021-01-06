import socket
import threading

# ustalamy wielkość headera, który będzie pierwszą wiadomością od klienta, ta wiadomość będzie nam mówić jakiej wielkości
# będzie normalna (nie poprzedzająca wiadomość) jaką klient nam wysyła
HEADER = 64
PORT = 5050
SERVER = "192.168.56.1" # Wyciągamy lokalny adres IPv4
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
print(socket.gethostname())
print(SERVER)

# tworzymy nowe gniazdo, podając specyfikację jakie typy adresów akceptujemy
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# łączymy gniazdo ze stworzonym adresem, który składa się z serwera oraz portu
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    # czekamy aż otrzymamy informacje od klienta
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # blocking line of code, nic się nie stanie dopóki nie dostaniemy wiadomości od klienta
        # jako parametr przyjmuje ilość bajtów jaką akceptujemy w wiadomości
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen() # nasłuchujemy nowych połączeń
    print(f"[LISTENING] Server is listening on  {SERVER}")
    while True:
        conn, addr = server.accept() # connection i address będą potrzebne do komunikacji w drugą stronę
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # tworzymy nowy wątek do obsługi nowego klienta
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # Sprawdzamy ile wątków obsługuje proces
        # tego programu oprócz wątku start, który nasłuchuje nowych połączeń
        # każdy klient dostaje 1 wątek


print("[STARTING] Server is starting...")
start()

