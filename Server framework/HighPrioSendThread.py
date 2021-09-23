import threading
import socket

recvsize = 512
localHost = "127.0.0.1"


# High priority messages only, expects a response for every sent message
class UDPHighPrioritySendThread(threading.Thread):
    def __init__(self, data, address):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = data
        self.address = address

    def run(self):
        self.sock.settimeout(3)
        s_address = (localHost, 0)  # 0 for any available port
        self.sock.bind(s_address)
        print("Handling send data to client")
        print("Sending high priority response")
        while True:
            try:
                self.sock.sendto(self.data.encode(), self.address)
                revData, retaddress = self.sock.recvfrom(recvsize)
                if "OK" in revData.decode():
                    print("Received confirmation")
                    break
            except socket.timeout:
                print("Time-out occurred, resending")
                pass
