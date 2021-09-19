import socket


localHost = "127.0.0.1"
localPort = 5552
testMessage = b"Please help me, there is a bear running at m-"

def bootClient():
    print("Booting up Lost and Found test client")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(testMessage, (localHost, localPort))
    print("Sent message to server")
    data, address = sock.recvfrom(1024)
    print(data.decode())
    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == "__main__":
    bootClient()