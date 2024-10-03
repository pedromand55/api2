#Lavet af Lukas
import multiprocessing as mp
import math
import time
import psutil


def complex_math(dummy_arg):
    i = 1000000  # Example number to perform complex math on
    """Perform complex math operations on a single number."""
    result = math.sqrt(i) * math.sin(i) * math.cos(i) * math.tan(i) + math.exp(math.sin(i/1000))
    for j in range(100):
        result += math.log(abs(math.sin(i+j)) + 1e-10) * math.cos(j)
    return result

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def worker():
    result = fibonacci(35)
    core_affinity = psutil.Process().cpu_affinity()
    print(f"Result: {result}, Running on core: {core_affinity }")

def set_affinity(process, cores):
    psutil.Process(process.pid).cpu_affinity(cores)

def main():
    # Get the number of available CPU cores
    total_cores = psutil.cpu_count(logical=False)
    
    # Ask user for the number of cores to use (max 2)

    num_cores = psutil.cpu_count()
    pool = mp.Pool(2)

    
    print(f"Using {num_cores} cores for the process")

    last_two_cores = list(range(num_cores - 2, num_cores))

    for process in pool._pool:
        print("test")
        set_affinity(process, last_two_cores)

    # Define the total range
    # total_range = 10**6

    # Create a pool of worker processes
    # with mp.Pool(processes=num_cores) as pool:
        # Use pool.map to apply complex_math to each number in the range
        #r esults = pool.map(complex_math, range(total_range))

    # pool.map(complex_math, range(1000))

    results = [pool.apply_async(worker) for _ in range(100)]


    for result in results:
        result.get()  # Wait for the worker processes to finish

    pool.close()
    pool.join()

    # Sum up all the results
    # total_result = sum(results)

    # print(f"Final result: {total_result}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
