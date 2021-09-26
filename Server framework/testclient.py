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
    sock.settimeout(5)
    try:
        #sock.sendto(testMessage, (localHost, localPort))
        lostmsg1 = b"HIGH,lost,k3442,52.99,90.50"
        lostmsg2 = b"HIGH,lost,e4442,6332.69,7.00"
        foundmsg = b"HIGH,found,k3442"
        lowmsg = b"Low"
        sock.sendto(lostmsg1, (localHost, localPort))
        print("Sent message to server: " + lostmsg1.decode())
        data, address = sock.recvfrom(512)
        print("Received the following reply: " + data.decode())

        sock.sendto(lowmsg, (localHost, localPort))
        print("Sent message to server: " + lowmsg.decode())
        ##time.sleep(7) #sleep to test resend
        dataHigh, addressHigh = sock.recvfrom(512)
        print("Received the following reply: " + dataHigh.decode())
        sock.sendto(okmes, addressHigh)
        print("Sent message to server: " + okmes.decode())

    except socket.timeout:
        print("timed out")
    print("Closing client")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


if __name__ == "__main__":
    bootClient()
