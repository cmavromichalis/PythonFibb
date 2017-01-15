import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8090))

number = 4
client_socket.send(number.to_bytes(32, byteorder='little', signed=False))
print('Sent the number: ', number)

while True:
    print('Waiting for a response...')
    buffer = client_socket.recv(32)
    fibonnachi_number = int.from_bytes(buffer, byteorder='little', signed=False)
    print('Calculated Fibonnachi number : ', fibonnachi_number)
    break

