import socket
import threading


nickname = input("Choose your nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Request sent")
client.connect(('127.0.0.1', 55555))
print("Connected")


def receive():
    while True:
        try:
          
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        mess = message.split()
        mess1 = mess[1]
        if mess1 == "exit":
            client.send(message.encode('ascii'))
            client.close()
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()