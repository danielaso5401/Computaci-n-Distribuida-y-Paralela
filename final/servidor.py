import socket
import threading
import sys
import pickle

class Servidor():
	def __init__(self, host="localhost", port=4000):

		self.clientes = []
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)
		
	def aceptarCon(self):
		print("aceptarCon iniciado")
		a=True
		while a==True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clientes.append(conn)
				a=False
			except:
				pass

	def procesarCon(self):
		print("ProcesarCon iniciado")
		if len(self.clientes) > 0:
			for c in self.clientes:
				try:
					data = c.recv(1024)
					if data:
						return(pickle.loads(data))
				except:
					pass



