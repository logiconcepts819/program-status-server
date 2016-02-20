import socket
from socket_util import recvall
from led_state import LEDState
from threading import Thread
from __init__ import PORT, BACKLOG
import struct

class ClientSession:
    def __init__(self, parent, conn, index):
        self.parent = parent
        self.conn = conn
        self.index = index
        
        self.thread = Thread(target=self.handle_request)
        self.thread.daemon = True
        self.thread.start()
    
    def close_session(self):
        try:
            self.conn.shutdown(socket.SHUT_RDWR)
            self.conn.close()
        except socket.error:
            pass
        self.thread.join()
    
    def handle_request(self):
        conn_closed = False
        while not conn_closed:
            raw_value = None
            try:
                raw_value = recvall(self.conn, 4)
            except socket.error:
                pass
            
            if raw_value is None or len(raw_value) < 4:
                conn_closed = True
            
            if not conn_closed:
                value = struct.unpack('>f', raw_value)[0]
                self.parent.led_state.set_status(self.index, value)

        self.parent.sessions[self.index] = None

class ExitCodeServer:
    def __init__(self, led_pairs):
        self.led_pairs = led_pairs
        self.led_state = LEDState(led_pairs)
        self.sessions = [None]*len(led_pairs)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', PORT))
        self.s.listen(BACKLOG)
    
    def loop(self):
        while True:
            conn, _ = self.s.accept()
            
            found_space = False
            index = 0
            for session in self.sessions:
                if session is None:
                    found_space = True
                    break
                else:
                    index += 1
            
            if found_space:
                self.sessions[index] = ClientSession(self, conn, index)
            else:
                try:
                    conn.close()
                except socket.error:
                    pass

    def shutdown(self):
        for session in self.sessions:
            if session is not None:
                session.close_session()
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
        self.led_state.cleanup()
