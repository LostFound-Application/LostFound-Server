import socket
import time
from ServerListenThread import UDPServerListenThread
from ServerSendThread import UDPServerSendThread


localHost = "127.0.0.1"


def bootServer():  # Boots the server with a listening, sending and a API thread
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localPort = 5552#random.randint(3000, 6000)
    s_address = (localHost, localPort)
    print("Booting up Lost and Found server")
    sock.settimeout(2)
    sock.bind(s_address)
    listenThread = UDPServerListenThread(sock)
    sendThread = UDPServerSendThread(sock)
    listenThread.start()
    sendThread.start()

    while True:
        stopInput = input("Type 'stop' to stop the server.")
        if "stop" in stopInput:
            listenThread.killThread()
            sendThread.killThread()
            print("Please wait shortly to close the sockets properly")
            time.sleep(3)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            print("Sockets closed, exiting server")
            quit()


if __name__ == "__main__":
    bootServer()
