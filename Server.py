import socket
import threading


host = '127.0.0.1'
port = 55555


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            
            message = client.recv(1024)
            broadcast(message)
        except:
            
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            print(nickname,"left!!")
            nicknames.remove(nickname)
            break

def closing():
    inp = input()
    if inp == "exit":
        server.close()

def receive():
    while True:
       
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

       
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

thread1 = threading.Thread(target = closing)
thread1.start()
receive()