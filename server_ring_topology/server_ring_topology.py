import socket
import _thread
import time


def start_servers(servers):
	for index in range(numberOfServers):
		servers.append(start_server(IP, STARTING_PORT + (index * 100)))


def start_server(IP, PORT):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((IP, PORT))
	sock.listen(1)
	print(f'Started {sock.getsockname()}...')
	return sock


def connect_servers(connections):
	for index in range(numberOfServers):
		connections.append(connect_to_next(IP, STARTING_PORT if (index == numberOfServers-1) else STARTING_PORT + (index + 1) * 100))


def connect_to_next(IP, PORT):
	nextSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	nextSock.connect((IP, PORT))
	print(f'Connected to {nextSock.getpeername()}...')
	return nextSock


def send_messages(servers, connections):
	for i in range(numberOfServers):
		try:
			messages[i] = input(f"\nEnter message {servers[i].getsockname()}: ")
			connections[i].sendall(str.encode(messages[i], "utf-8"))
			time.sleep(5)
		except Exception as e:
			print(e)	


def start_recv_threads(servers, connections):
	for i in range(numberOfServers):
		_thread.start_new_thread(pass_received_message, (servers[i], connections[i], i))


def pass_received_message(server, nextSocket, serverID):
	try:
		previous, _ = server.accept()

		while True:
			msg = previous.recv(1024).decode("utf-8")
			if msg == messages[serverID]:
				print(f'Message {msg} passed through ring! {server.getsockname()} received his message.')
				messages[serverID] = ""
			else:
				print(f'Message {msg} received. {server.getsockname()} passing to {nextSocket.getpeername()}.')
				nextSocket.sendall(str.encode(msg, "utf-8"))
	except Exception as e:
		print(e)


def main():

	servers = []
	connections = []

	start_servers(servers)
	connect_servers(connections)
	start_recv_threads(servers, connections)

	while True:
		send_messages(servers, connections)


if __name__  == "__main__":
	IP = "127.0.0.1"
	STARTING_PORT = 40101
	numberOfServers = int(input('Enter number of servers: '))
	print('\r')
	
	messages = [None] * numberOfServers

	main()

