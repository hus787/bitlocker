import subprocess
import time
import pyautogui

def run_command_and_interact(command, prompt_responses):
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
        time.sleep(2)  # Wait for the command prompt to open and the initial command to run

        # Iterate through the prompt responses and send them to the command prompt
        for response in prompt_responses:
            pyautogui.typewrite(response + '\n') #type the response and press enter
            time.sleep(1) # wait between responses

        # Optionally, you can wait for the process to finish
        # process.wait()

    except FileNotFoundError:
        print("Command prompt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
command_to_run = "python my_script.py" #or anything else
responses = ["input1", "input2", "input3"]

# Create a simple python script for testing.
with open("my_script.py", "w") as f:
    f.write("input1 = input('Enter input 1: ')\n")
    f.write("input2 = input('Enter input 2: ')\n")
    f.write("input3 = input('Enter input 3: ')\n")
    f.write("print(f'Input 1: {input1}, Input 2: {input2}, Input 3: {input3}')\n")

run_command_and_interact(command_to_run, responses)

#cleanup the temporary file
import os
os.remove("my_script.py")

#Example for ping
#run_command_and_interact("ping 127.0.0.1 -t", ["CTRL+C"]) # example using CTRL+C. Note that CTRL+C is not a regular string, and requires special handling.
#run_command_and_interact("ping 127.0.0.1 -t", []) #example with no responses.
