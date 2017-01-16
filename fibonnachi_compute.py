import time


# Function that will calculate and return the n'th Fibonacci number.
def fibonacci_generator(number):
    # Validate input
    if number <= 0:
        return 0

    # Calculation loop
    a = 0
    b = 1
    counter = 1

    start_time = time.time()
    while counter < number:
        # One liner:
        a, b = b, a + b
        # old_b = b
        # b += a
        # a = old_b
        counter += 1
    end_time = time.time()
    print("Calculated Fibonnachi number", number, ":", b)
    print("Total time taken to calculate loop: ", end_time - start_time)
    return b
