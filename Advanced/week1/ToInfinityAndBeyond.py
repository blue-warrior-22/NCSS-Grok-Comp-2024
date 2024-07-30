import time

count = 0
total = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

timeout = 2
start_time = time.time()

while count < len(numbers):
    if numbers[count] % 2 == 0:
        total += numbers[count]
    
    # Increment count on every loop iteration
    count += 1
    
    # Break if the program runs longer than the timeout
    if time.time() - start_time > timeout:
        break

print(total)
