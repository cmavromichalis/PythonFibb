from fibonnachi_compute import fibonacci_generator
import socket
import threading


class FibonnachiServer(threading.Thread):

    def __init__(self, this_host, this_port, this_socket):
        threading.Thread.__init__(self)
        self.host = this_host
        self.port = this_port
        self.socket = this_socket
        print("New thread started for " + ip + ":" + str(port))

    def run(self):
        buffer = self.socket.recv(1024)

        if len(buffer) > 0:
            received_number = int.from_bytes(buffer,
                                             byteorder='little',
                                             signed=False)

            # Check the bytes we received are actually a unsigned number.
            # Otherwise send back 0
            if (type(received_number) != int) or (received_number < 0):
                print(received_number, 'is not a unsigned, whole number.')
                self.socket.send(b'\x00\x00')
                self.socket.close()
            else:
                print('Received number: ', received_number)

                try:
                    number = fibonacci_generator(received_number)
                    fibonnachi_number_bytes = number.to_bytes(
                        ((number.bit_length() + 7) // 8),
                        byteorder='little',
                        signed=False)
                    print('Calculated Fibonnachi number: ', number)

                    # Grab chunks of bytes and transmit until there are no more
                    i = 0
                    byte_chunk = fibonnachi_number_bytes[i:i + 1024]
                    while byte_chunk != b'':
                        i += 1024
                        self.socket.send(byte_chunk)
                        print('Calculated chunks: ', byte_chunk)
                        byte_chunk = fibonnachi_number_bytes[i:i + 1024]
                    self.socket.close()

                except Exception as e:
                    print('Exception occurred: ', e)
                    self.socket.close()


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('localhost', 8080))
threads = []

while True:
    my_socket.listen(4)
    print("\nListening for incoming connections...")
    (client_sock, (ip, port)) = my_socket.accept()
    new_thread = FibonnachiServer(ip, port, client_sock)
    new_thread.start()
    threads.append(new_thread)
