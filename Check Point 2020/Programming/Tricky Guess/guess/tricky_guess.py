from collections import Counter
import socket

class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):

        self.socket.send(data)

    def close(self):

        self.socket.close()

def shared_chars(s1, s2):
	return sum((Counter(s1) & Counter(s2)).values())

with open('words.txt', 'r') as a_file:
	nc = Netcat('tricky-guess.csa-challenge.com', 2222)
	print (nc.read())
	nc.read()
	amount = 0
	lastString = ''
	for line in a_file:
		stripped_line = line.strip()
		if shared_chars(stripped_line,lastString)>=amount:
			nc.write(str.encode(stripped_line+ '\n'))
			amount = int(nc.read().decode())
			lastString = stripped_line
