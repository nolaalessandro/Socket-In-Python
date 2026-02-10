import socket

indirizzo_ip = '127.0.0.1'
porta = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((indirizzo_ip, porta))

# 3. INVIO (Esercizio 1: messaggio dinamico)
testo = input("Scrivi qualcosa da inviare al server: ")
client.send(testo.encode('utf-8'))

# 4. RICEZIONE RISPOSTA (La parte dell'Esercizio 2)
risposta_server = client.recv(1024).decode('utf-8')
print(f"Risposta dal Server: {risposta_server}")

client.close()