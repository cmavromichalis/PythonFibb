## Synopsis

This is a Python 3.6.0 client and server. The client will pass a number n to the server and the server will then compute the nth Fibonacci number and return it to the client.

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

This is a coding exercise for a pretty cool job :)

## Installation

This is built with Python 3.6.0 and uses only standard modules from it.

1) First, make sure Python 3.6.0 is downloaded and installed.
2) Check git is also installed
3) git clone https://github.com/cmavromichalis/PythonFibb.git
4) cd PythonFibb/
5) ./runserver.sh &
6) python3 socket_client.py 10000

## Description

If there is an issue computing the nth Fibonacci, the server will return the value 0
The server will listen for connections on port 8080 and expects to receive in bytes an unsigned integer

## Tests

Describe and show how to run the tests with code examples.

## License

MIT
