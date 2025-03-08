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



def run_command_and_interact(command, response):
    """
    Runs a Windows command in a new command prompt and interacts with it.

    Args:
        command: The command to execute as a string.
        prompt_responses: A list of strings, each representing a response to a prompt.
    """

    try:
        # Start the command in a new command prompt
        process = subprocess.Popen(['cmd', '/k', command], creationflags=subprocess.CREATE_NEW_CONSOLE)

        # Give the command prompt time to open and the command to start. Adjust as needed.
        time.sleep(1)  # Wait for the command prompt to open and the initial command to run
        
        pyautogui.typewrite(response + '\n') #type the response and press enter
        process.poll()  # Check if process has finished
        exit_code = process.returncode

        if exit_code == 0:
            print("-" * 80) #long line
    except FileNotFoundError:
        print("Command prompt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage to print generated passwords
if __name__ == "__main__":
    for pwd in generate_passwords():
        print(pwd)
        command_to_run = "manage-bde.exe -unlock d: -pw" #or anything else
        run_command_and_interact(command_to_run, pwd)

#Example for ping
#run_command_and_interact("ping 127.0.0.1 -t", ["CTRL+C"]) # example using CTRL+C. Note that CTRL+C is not a regular string, and requires special handling.
#run_command_and_interact("ping 127.0.0.1 -t", []) #example with no responses.
