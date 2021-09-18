import socket


localHost = "127.0.0.1"
testMessage = b"Please help me, there is a bear running at m-"

def bootClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localPort = 5552#random.randint(3000, 6000)
    s_address = (localHost, localPort)
    print("Booting up Lost and Found test client")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(testMessage, (localHost, localPort))
    print("Sent message to server")
    # data, address = data, address = sock.recvfrom(1024)
    # print(data.decode())
    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == "__main__":
    bootClient()