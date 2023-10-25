import ssl
import socket

def collect_shares_from_patients(port, cert, key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert, keyfile=key)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification for self-signed certs

    print(f"Listening on port {port}...\n")

    shares = 0

    for i in range(2):
        client_socket, _ = server_socket.accept()
        client_socket = context.wrap_socket(client_socket, server_side=True)

        data = client_socket.recv(1024).decode()
        print(f"Received from patient : {data}\n")
        shares += int(data)

        response = "The share was received"
        client_socket.send(response.encode())
        client_socket.close()
    
    #print(f"Shares received from other patients {str(shares)}\n")
    
    return shares