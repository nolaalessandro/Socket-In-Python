import socket

# Creiamo il socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ci connettiamo al server
client.connect(('127.0.0.1', 5000))

# Inviamo un messaggio (bisogna trasformarlo in byte con .encode)
testo = "Ciao classe! Questo messaggio viaggia su TCP."
client.send(testo.encode('utf-8'))

client.close()