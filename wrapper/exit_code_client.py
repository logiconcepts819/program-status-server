from __init__ import HOST, PORT
import socket
import struct

class ExitCodeClient:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((HOST, PORT))
            self.connected = True
        except socket.error:
            print("Warning: Could not connect to server at %s:%d"%(HOST, PORT))
            self.connected = False
    
    def send_status(self, new_status):
        if self.connected:
            try:
                self.s.sendall(struct.pack('>f', float(new_status)))
            except socket.error:
                print("Warning: Client is now disconnected")
                self.connected = False
    
    def shutdown(self):
        if self.connected:
            try:
                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
            except socket.error:
                pass
            self.connected = False