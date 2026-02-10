import socket

indirizzo_ip = '127.0.0.1'
porta = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((indirizzo_ip, porta))
server.listen(1)

print(f"Server Eco avviato su {indirizzo_ip}:{porta}...")
print("In attesa di un messaggio dal client...")

# 2. Accetta la connessione
connessione, indirizzo_client = server.accept()
print(f"Connesso con il client: {indirizzo_client}")

# 3. Ricezione del messaggio
dati_ricevuti = connessione.recv(1024).decode('utf-8')
print(f"Messaggio ricevuto dal client: {dati_ricevuti}")

# 4. RISPOSTA (La parte dell'Esercizio 2)
risposta = f"Ciao Client! Ho ricevuto il tuo messaggio: '{dati_ricevuti}'"
connessione.send(risposta.encode('utf-8'))
print("Risposta di conferma inviata al client.")

# 5. Chiusura
connessione.close()
server.close()