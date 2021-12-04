from socket import *

from TCPStringServerPersistentMultithread import serverSocket

serverPort=5000
ServerSocket = socket(AF_INET ,SOCK_STREAM)
ServerSocket.bind(('',serverPort))
ServerSocket.listen(1)
print("The server is ready to receive.")
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence=="Quit":
            print("Done with one client.")
            connectionSocket.close()
            break
        else:
            capitalizedSentence=sentence.uppuer()
            connectionSocket.send(capitalizedSentence.encode())