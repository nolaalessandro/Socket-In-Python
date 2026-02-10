import socket

# Creiamo il socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Colleghiamo il server all'indirizzo locale sulla porta 5000
server.bind(('127.0.0.1', 5000))
server.listen(1)
print("Server avviato... in attesa del client")

# Accettiamo la connessione
connessione, indirizzo = server.accept()
print(f"Connesso a: {indirizzo}")

# Riceviamo il messaggio (max 1024 byte) e lo decodifichiamo
messaggio = connessione.recv(1024).decode('utf-8')
print(f"Messaggio ricevuto: {messaggio}")

connessione.close()
server.close()