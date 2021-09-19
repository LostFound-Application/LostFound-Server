import threading
import collections
import socket
from ServerSendThread import UDPServerSendThread

recvsize = 1024


class ServerAPIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keepworking = True
        self.linkedList = collections.deque()
        self.sendThread = UDPServerSendThread(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))

    def run(self):
        print("Handling API requests from client")
        messageOK = b"I am the bear."
        self.sendThread.start()
        while self.keepworking:
            if self.linkedList:
                print("Processing API request, API request:")
                print(self.linkedList[-1][0])
                self.sendThread.addSendRequest(messageOK, self.linkedList[-1][1])
                self.linkedList.pop()

    def addAPIRequest(self, request, address):
        self.linkedList.append((request, address))

    def killThread(self):
        self.keepworking = False
        self.sendThread.killThread()
        print("API Thread is killed")
