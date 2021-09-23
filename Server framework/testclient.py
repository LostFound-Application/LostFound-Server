import socket
import time
localHost = "127.0.0.1"
localPort = 5553
testMessage = b"Please help me, there is a bear running at m-"
testHigh = b"HIGH"
okmes = b"OK"


def bootClient():
    print("Booting up Lost and Found test client")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(testMessage, (localHost, localPort))
    print("Sent message to server: " + testMessage.decode())
    data, address = sock.recvfrom(512)
    print("Received the following reply: " + data.decode())

    sock.sendto(testHigh, (localHost, localPort))
    print("Sent message to server: " + testHigh.decode())
    time.sleep(7) #sleep to test resend
    dataHigh, addressHigh = sock.recvfrom(512)
    print("Received the following reply: " + dataHigh.decode())
    sock.sendto(okmes, addressHigh)
    print("Sent message to server: " + okmes.decode())

    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


if __name__ == "__main__":
    bootClient()
