import cProfile
import matplotlib.pyplot as plt


# Function to calculate the factorial of a number
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n

# Function to count iterations
def counter(n):
    count = 0
    for i in range(n):
        count += 1
    return count

def profile_and_plot():
    key_spaces = [7, 8, 9, 10, 11]  # Example key-space values

    # Measure time complexity for each key-space value
    time_complexities = []
    factorial_results = []
    for key_space in key_spaces:
        # Profiling the execution of counter(factorial(key_space))
        profiler = cProfile.Profile()
        profiler.enable()
        counter(factorial(key_space))
        profiler.disable()

        # Get time complexity information
        time_complexities.append(profiler.getstats()[0].totaltime)
        
        # Calculate factorial result out of profiling
        factorial_result = factorial(key_space)
        factorial_results.append(factorial_result)
        print(f"Factorial({key_space}) = {factorial_result}")

    # Plotting the time complexity bar graph
    plt.bar(key_spaces, time_complexities)
    plt.xlabel('Key-space')
    plt.ylabel('Time Complexity')
    plt.title('Time Complexity per Key-space')
    
    for i in range(len(key_spaces)):
        plt.text(key_spaces[i], time_complexities[i], str(factorial_results[i]))
    
    plt.show()
    
if __name__ == "__main__":
    profile_and_plot()
