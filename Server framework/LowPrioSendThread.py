import threading
import collections

recvsize = 512


# sends out the data, does not expect a reply, seen low priority it unimportant if the data gets properly received alway

class UDPLowPrioritySendThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
        self.keepworking = True
        self.linkedList = collections.deque()

    def run(self):
        print("Handling send data to client")
        while self.keepworking:
            if self.linkedList:
                print("Sending low priority response")
                self.sock.sendto(self.linkedList[-1][0], self.linkedList[-1][1])
                self.linkedList.pop()

    def addSendRequest(self, request, address):
        self.linkedList.append((request, address))

    def killThread(self):
        self.keepworking = False
        print("Send Thread is killed")
