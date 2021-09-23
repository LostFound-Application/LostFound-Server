import threading
import collections
import socket
from LowPrioSendThread import UDPLowPrioritySendThread
from HighPrioSendThread import UDPHighPrioritySendThread

recvsize = 1024


class ServerAPIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keepworking = True
        self.linkedList = collections.deque()
        self.sendThread = UDPLowPrioritySendThread(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))

    def run(self):
        print("Handling API requests from client")
        messageOK = b"I am the bear."
        self.sendThread.start()
        while self.keepworking:
            if self.linkedList:
                print("Processing API request, API request:")
                print(self.linkedList[-1][0])
                if "HIGH" in self.linkedList[-1][0]:
                    self.highPriorityMessage(messageOK, self.linkedList[-1][1])
                    self.linkedList.pop()
                else:
                    self.sendThread.addSendRequest(messageOK, self.linkedList[-1][1])
                    self.linkedList.pop()

    def addAPIRequest(self, request, address):
        self.linkedList.append((request, address))

    def highPriorityMessage(self, data, address):
        testMessage = "OH BOI"
        highPrioThread = UDPHighPrioritySendThread(testMessage, address)
        highPrioThread.start()

    def killThread(self):
        self.keepworking = False
        self.sendThread.killThread()
        print("API Thread is killed")
