import subprocess
import time
import pyautogui
import itertools

def generate_passwords():
    first_chars = ['M', 'm', 'R', 'r', 'S', 's', 'P', 'p']
    second_chars = ['-', '_', '']
    digits = [f"{i:04d}" for i in range(10000)]  # Generates 0000 to 9999

    for first, second, digit in itertools.product(first_chars, second_chars, digits):
        password = f"{first}{second}{digit}"
        yield password
def generate_passwords3():
    first_chars = ['M']
    second_chars = ['-', '_', '']
    digits = [f"{i:04d}" for i in range(100)]  # Generates 0000 to 9999
    passwords = []
    for first, second, digit in itertools.product(first_chars, second_chars, digits):
        password = f"{first}{second}{digit}"
        passwords.append(password)
    return passwords + ['Aa 12345678.']
    
def generate_passwords2():
    first_chars = ['P', 'p', 'M', 'm', 'R', 'r', 'S', 's', 'ر','پ','س','م']
    second_chars = ['-', '_', '']
    digits = ["2541","5498","1388","1396","1370","3652","6509","1358"]

    for first, second, digit in itertools.product(first_chars, second_chars, digits):
        password = f"{first}{second}{digit}"
        yield password
def generate_passwords4():
    first_chars = ['P', 'p', 'M', 'm', 'R', 'r', 'S', 's', 'ر','پ','س','م']
    second_chars = ['-', '_', '']
    digits = [f"{i:04d}" for i in range(10000)]  # Generates 0000 to 9999
    passwords = []
    for first, second, digit in itertools.product(first_chars, second_chars, digits):
        password = f"{first}{second}{digit}"
        passwords.append(password)
    return passwords

def run_command_and_interact(command, response):
    """
    Runs a Windows command in a new command prompt, interacts with it by typing the response,
    waits for a reasonable amount of time, then closes the command prompt.

    Args:
        command: The command to execute as a string.
        response: A string response to type into the prompt.
    """
    try:
        # Start the command in a new command prompt
        process = subprocess.Popen(['cmd', '/k', command], creationflags=subprocess.CREATE_NEW_CONSOLE)

        # Wait for the command prompt to open and the command to start.
        time.sleep(1)
        
        # Send the response (password) and press enter
        pyautogui.typewrite(response + '\n')
        
        # Wait for the command to process the input (adjust the duration as needed)
        time.sleep(2)
        
        # Terminate the command prompt window
        process.terminate()
        process.wait()
        
        print("-" * 80)  # print a long line after process termination
    except FileNotFoundError:
        print("Command prompt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage to print generated passwords
if __name__ == "__main__":
    for pwd in generate_passwords4():
        print(pwd)
        command_to_run = "manage-bde.exe -unlock d: -pw" #or anything else
        run_command_and_interact(command_to_run, pwd)

#Example for ping
#run_command_and_interact("ping 127.0.0.1 -t", ["CTRL+C"]) # example using CTRL+C. Note that CTRL+C is not a regular string, and requires special handling.
#run_command_and_interact("ping 127.0.0.1 -t", []) #example with no responses.
