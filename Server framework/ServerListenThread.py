import socket
import threading
from ServerLAPIThread import ServerAPIThread
from LowPrioSendThread import UDPLowPrioritySendThread
recvsize = 512


class UDPServerListenThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
        self.keepworking = True
        self.apiThread = ServerAPIThread()

    def run(self):
        print("Handling input data from client")
        self.apiThread.start()
        while self.keepworking:
            try:
                data, address = self.sock.recvfrom(recvsize)
                if data is not None:
                    print("Received data, forwarded  to API!")
                    self.apiThread.addAPIRequest(data.decode(), address)
                elif self.keepworking is False:
                    break
            except socket.timeout:
                pass


    def killThread(self):
        self.keepworking = False
        self.apiThread.killThread()
        print("Listen Thread is killed")
