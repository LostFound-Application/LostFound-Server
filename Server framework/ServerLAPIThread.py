import threading
import collections

recvsize = 1024


class ServerAPIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keepworking = True
        self.linkedList = collections.deque()

    def run(self):
        print("Handling API requests from client")
        while self.keepworking:
            if self.linkedList:
                print(self.linkedList[-1])

                self.linkedList.pop()

    def addAPIRequest(self, request):
        self.linkedList.append(request)

    def killThread(self):
        self.keepworking = False

        print("API Thread is killed")
