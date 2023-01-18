import sys
import socket
#Серверная сторона
print("WELCOME to SERVER side")

sock = socket.socket()      #создаем обьект сокет
# или можно так sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))       #биндим в виде кортежа адрес и порт на сокет
sock.listen(5)      #listen for clients with 5 connection in queue
connection = True
while connection:
    conn, addr = sock.accept()  # получаем клиентский сокет и адрес
    with conn:
        print(f"connected: {addr}")
        execute = True
        data = ""
        msg = ""
        while execute:
            data = conn.recv(2000)      #получить данные в байт
            try:
                msg = data.decode()
                msg = msg.strip()
                if msg.lower() == "exit":
                    execute = False
                elif msg.lower() == "sock_close":
                    execute = False
                else:
                    print(f"Received data: {msg}")
                    msg = f"{msg}"
                    conn.send(msg.encode())
                    print(f"Sent message: {msg}")
            except:
                print(sys.exc_info())

        # conn.close() #  надо закрывать соединение