# import socket

# def client_program():
#     host = 'localhost'  
#     port = 12345        

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     client_socket.connect((host, port))

#     message = "Olá, servidor no container!"
#     client_socket.send(message.encode())

#     data = client_socket.recv(1024)
#     print(f"Resposta do servidor: {data.decode()}")

#     client_socket.close()

# if __name__ == "__main__":
#     client_program()
