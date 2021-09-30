import socket
import time

localHost = "127.0.0.1"
localPort = 5553
testMessage = b"Please help me, there is a bear running at m-"
okmes = b"OK"


def bootClient():
    print("Booting up Lost and Found test client")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    try:
        # sock.sendto(testMessage, (localHost, localPort))
        lostmsg1 = "lost,k3442,52.99,90.50"
        lostmsg2 = "lost,e4442,6332.69,7.00"
        update = "updateme"
        foundmsg = "found,k3442"
        foundmsg2 = "found,e4442"

        sock.sendto(foundmsg2.encode(), (localHost, localPort))
        print("Sent message to server: " + lostmsg1)
        data, address = sock.recvfrom(512)
        print("Received the following reply: " + data.decode())
        # sock.sendto(okmes, address)
        # print("Sent message to server: " + okmes.decode())


    except socket.timeout:
        print("timed out")
    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


if __name__ == "__main__":
    bootClient()
