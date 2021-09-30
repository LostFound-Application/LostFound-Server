import threading
import collections
import socket
from LowPrioSendThread import UDPLowPrioritySendThread
from HighPrioSendThread import UDPHighPrioritySendThread
from Database import Methods
import datetime

recvsize = 1024


class ServerAPIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.keepworking = True
        self.linkedList = collections.deque()
        self.sendThread = UDPLowPrioritySendThread(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
        #NEW
        Methods.initiateDatabase()

    def run(self):
        print("Handling API requests from client")
        messageOK = "I am the bear." #changed from bit to string
        self.sendThread.start()
        while self.keepworking:
            if self.linkedList:
                print("Processing API request, API request:")
                print(self.linkedList[-1][0])
                if "lost" in self.linkedList[-1][0]:
                    # add a lost person to the database
                    self.addLostPerson(self.linkedList[-1][0])
                    self.getLostLocations()
                    self.highPriorityMessage("Added as lost, stay still", self.linkedList[-1][1])
                    self.linkedList.pop()
                elif "found" in self.linkedList[-1][0]:
                    self.personFound(self.linkedList[-1][0])
                    self.highPriorityMessage("You have been found", self.linkedList[-1][1])
                    self.linkedList.pop()
                elif "updateme" in self.linkedList[-1][0]:
                    self.sendThread.addSendRequest(str(self.getLostLocations()), self.linkedList[-1][1])
                    self.linkedList.pop()
                else:
                    self.sendThread.addSendRequest("Invalid API request", self.linkedList[-1][1])
                    self.linkedList.pop()

    def addAPIRequest(self, request, address):
        self.linkedList.append((request, address))

    def addLostPerson(self, data):
        dataparts = data.split(",")
        x = datetime.datetime.now()
        dtime = x.strftime("%H.%M %d.%m.%Y")
        location = (dataparts[1], dataparts[2], dataparts[3], dtime, 1)
        Methods.addNewLocation(location)
    
    def personFound(self, data):
        dataparts = data.split(",")
        id = (dataparts[1])
        Methods.deleteByClientID(id)
        print(id)

    def getLostLocations(self):
        vals = Methods.getLostLocations()
        return vals

    def highPriorityMessage(self, data, address):
        highPrioThread = UDPHighPrioritySendThread(data, address)
        highPrioThread.start()

    def killThread(self):
        self.keepworking = False
        self.sendThread.killThread()
        print("API Thread is killed")
