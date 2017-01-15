import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

number = 10
client_socket.send(number.to_bytes(32, byteorder='little', signed=False))
print('Sent the number: ', number)

fibonnachi_number_bytes = b''

print('Waiting for a response...')
while True:
    buffer = client_socket.recv(1024)
    if buffer:
        fibonnachi_number_bytes += buffer[0:]
        print('Receiving response...')
    else:
        print('Calculated Fibonnachi number bytes: ', fibonnachi_number_bytes)
        fibonnachi_number = int.from_bytes(fibonnachi_number_bytes, byteorder='little', signed=False)
        print('Calculated Fibonnachi number : ', fibonnachi_number)
        break


