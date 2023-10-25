import socket
import ssl

def send_shares(port, name, cert, key, share):
    print(f"Connect to {name}\n")
    
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile=cert, keyfile=key)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification for self-signed certs

    client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    client_socket.connect(('localhost', port))

    print(f"Sending share {share} to {name}\n")
    client_socket.send(str(share).encode())

    data = client_socket.recv(1024).decode()
    print(f"Received from {name}: {data}\n")

    client_socket.close()