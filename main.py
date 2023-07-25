import subprocess
import shutil
import os
import sys
import pyautogui
import time
import pyperclip

def run_msi(msi_path):
    try:
        # Executes the MSI
        subprocess.run(['cmd', '/c', msi_path], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to run the MSI file.")
        sys.exit(1)

def copy_icon_to_temp(source_path, temp_directory):
    try:
        # Copies and pastes the icon to the right path
        shutil.copy(source_path, temp_directory)
    except FileNotFoundError:
        print("Error: Icon file not found.")
        sys.exit(1)
    except shutil.Error:
        print("Error: Failed to copy the icon file.")
        sys.exit(1)

def launch_run_dialog():
    # Simulate pressing the Windows key + R
    pyautogui.hotkey('win', 'r')

def type_text(text):
    # Simulate typing the specified text
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

# Time delay to give Run dialog time to open
delay_before_typing = 1

# Fetches the current path
script_directory = os.path.dirname(os.path.realpath(sys.argv[0]))

# Creates the MSI path
msi_path = os.path.join(script_directory, "ZeroTier One.msi")

# Icon's path
source_path = os.path.join(script_directory, "zerotier-tray-icon.ico")

# Takes the TEMP's user path
temp_directory = os.path.join(os.environ["TEMP"], "zerotier-tray-icon.ico")

# Executes the MSI
try:
    run_msi(msi_path)
    copy_icon_to_temp(source_path, temp_directory)
except KeyboardInterrupt:
    print("\nScript execution interrupted by user.")
    sys.exit(1)

# Launch the Run dialog
launch_run_dialog()

# Wait for a moment before typing to ensure Run dialog is active
time.sleep(delay_before_typing)

# Type 'cmd' in the Run dialog
type_text('cmd')

# Simulate pressing the 'Enter' key to execute the command
pyautogui.press('enter')
time.sleep(1)

# Path to the file that stores the network ID
network_id_path = os.path.join(script_directory, "Network_ID.txt")

# Reads the ID
try:
    with open(network_id_path) as file:
        network_id = file.read()
except FileNotFoundError:
    print("Error: Network ID file not found.")
    sys.exit(1)

# Type the 'rede.exe' command and execute it
type_text(f'zerotier-cli join {network_id}')
pyautogui.press('enter')

# Add a delay to give the 'rede.exe' program time to execute (adjust as needed)
time.sleep(5)

# Simulate pressing Alt+F4 to close the Command Prompt window
pyautogui.hotkey('alt', 'f4')
