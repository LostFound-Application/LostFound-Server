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
                self.linkedList.pop()

    def addSendRequest(self, request):
        self.linkedList.append(request)
    def killThread(self):
        self.keepworking = False
        print("Send Thread is killed")
