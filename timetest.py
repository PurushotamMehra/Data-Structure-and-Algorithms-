import time

def my_function():
    # Your function code here
    time.sleep(2)

# Record the start time
start_time = time.time()

# Call your function
my_function()

# Record the end time
end_time = time.time()

# Calculate the CPU execution time
execution_time = end_time - start_time

print("Execution Time: {:.2f} seconds".format(execution_time))
