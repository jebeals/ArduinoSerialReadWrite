import signal


class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

def input_with_timeout(prompt, timeout):
    # Set the signal handler and a timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    
    try:
        return input(prompt)
    except TimeoutException:
        print("\nInput timed out!")
        return None
    finally:
        signal.alarm(0)  # Disable the alarm

# # Example usage
# try:
#     user_input = input_with_timeout("Enter something: ", 5)
#     if user_input:
#         print(f"You entered: {user_input}")
#     else:
#         print("No input provided.")
# except TimeoutException:
#     print("User input timed out.")