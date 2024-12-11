# import socket

# def start_server():
#     host = '0.0.0.0' 
#     port = 12345       

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(1)

#     print(f"Servidor rodando no {host}:{port}, esperando por conexões...")

#     client_socket, client_address = server_socket.accept()
#     print(f"Conexão estabelecida com {client_address}")

#     data = client_socket.recv(1024)
#     print(f"Mensagem recebida do cliente: {data.decode()}")

#     response = "Mensagem recebida com sucesso!"
#     client_socket.send(response.encode())

#     client_socket.close()
#     server_socket.close()

# if __name__ == "__main__":
#     start_server()
