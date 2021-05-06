import socket
import threading
import sys
import pickle

class Cliente():
	def __init__(self, matriz_a, matriz_b, matriz_c, host="localhost", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))
		self.cadena=[matriz_a,matriz_b,matriz_c]
		self.send_msg(self.cadena)

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))
