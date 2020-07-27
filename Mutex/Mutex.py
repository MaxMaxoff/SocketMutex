#!/.venv/bin/python
# -*- coding: utf-8 -*-
import socket
import sys

# realize locking mechanism using sockets
class Mutex:
    def __init__(self, lock_name):
        self.lock_name = lock_name
        self.lock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    def set_lock(self):
        try:
            self.lock.bind('\0' + self.lock_name)
            return True
        except socket.error:
            return False
    
    def release_lock(self):
        try:
            self.lock.close()
            return True
        except socket.error as exc:
            return False
