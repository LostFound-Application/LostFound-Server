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

        sock.sendto(update.encode(), (localHost, localPort))
        print("Sent message to server: " + update)
        data, address = sock.recvfrom(512)
        part = data.decode()
        print("Received the following reply: " + part)
        # sock.sendto(okmes, address)
        # print("Sent message to server: " + okmes.decode())
        tuples = part[1:-1]
        tuples = tuples.split("),")
        for i in tuples:
            i = i.replace("(","")
            i = i.replace(")","")
            i = i.replace(" ", "")
            print(i)
        




    except socket.timeout:
        print("timed out")
    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


if __name__ == "__main__":
    bootClient()
