import threading
import collections
recvsize = 1024


class UDPServerSendThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
        self.keepworking = True
        self.linkedList = collections.deque()

    def run(self):
        print("Handling send data to client")
        while self.keepworking:
            if self.linkedList:
                print("Sending API bear response")
                self.sock.sendto(self.linkedList[-1][0], self.linkedList[-1][1])
                self.linkedList.pop()

    def addSendRequest(self, request, address):
        self.linkedList.append((request, address))
    def killThread(self):
        self.keepworking = False
        print("Send Thread is killed")
