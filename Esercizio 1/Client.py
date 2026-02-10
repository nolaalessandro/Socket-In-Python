import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

# Invece di un testo fisso, usiamo input()
testo = input("Scrivi un messaggio per il server: ")
client.send(testo.encode('utf-8'))

client.close()