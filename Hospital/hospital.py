import socket
import ssl

server_certfile = 'server-cert.pem'
server_keyfile = 'server-key.pem'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8090))
server_socket.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_certfile, keyfile=server_keyfile)

print("Hospital is listening on port 8090...\n")

shares = 0

for i in range(3):
    c_socket, addr = server_socket.accept()
    client_socket = context.wrap_socket(c_socket, server_side=True)

    data = client_socket.recv(1024).decode()
    print(f"Received from share from patient: {data}\n")
    shares += int(data)

    response = "Share received"
    client_socket.send(response.encode())
    client_socket.close()
print(f"Patients health secrets aggregated value: {shares}\n")