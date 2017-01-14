import ctypes
import time

# Hold the numbers we calculated already; has our seeds to start
FIBONACCI_NUMBERS = [0, 1]


# Function that will calculate and return the n'th Fibonacci number.
def fibonacci_generator(number):

    # Validate input
    if number <= 0:
        return 'Please enter a number greater than 0'

    # If we have already calculated this, return it
    if len(FIBONACCI_NUMBERS) >= number:
        print('Already calculated: ')
        return FIBONACCI_NUMBERS[number-1]

    # Else calculate it where we left off
    number_computed = len(FIBONACCI_NUMBERS)
    a = FIBONACCI_NUMBERS[number_computed - 2]
    b = FIBONACCI_NUMBERS[number_computed - 1]
    counter = number_computed

    # Calculation loop
    start_time = time.time()
    while counter < number:
        # One liner: a, b = b, a + b
        old_b = b
        b += a
        a = old_b
        counter += 1
        FIBONACCI_NUMBERS.append(b)
    end_time = time.time()
    print("total time taken this loop: ", end_time - start_time)
    return b


ct = ctypes.c_uint32(42)

# print("0'th num should be. ", fibonacci_generator(0))  # Error
# print("1st num should be. ", fibonacci_generator(1))  # 0
# print("1st num should be. ", fibonacci_generator(1))  # 0
# print("10 num should be. ", fibonacci_generator(10))  # 0
# print("20 num should be. ", fibonacci_generator(20))  # 0
# print("10 num should be. ", fibonacci_generator(10))  # 0
# print("42 num should be. ", fibonacci_generator(ct.value))  # 0
print("500000 num should be.", fibonacci_generator(500000))
