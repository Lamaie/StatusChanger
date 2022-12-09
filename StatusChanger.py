import pyautogui
import time
import os

# Get the current user
current_user = os.getenv("USERNAME")
pyautogui.FAILSAFE = True

# Function to change the Discord status
def change_status():
    # Get the input from the status field
    status = pyautogui.prompt(text="Status:", title="Discord Status Changer")

    # Check if Discord is already running
    if "Discord" in os.popen("tasklist").read():
        print("Discord is already running.")
        os.system(r"C:\Users\{}\AppData\Local\Discord\Update.exe --processStart Discord.exe".format(current_user))
        time.sleep(1)
    else:
        # Open Discord
        os.system(r"C:\Users\{}\AppData\Local\Discord\Update.exe --processStart Discord.exe".format(current_user))
        print("Discord has been opened.")
        time.log(5) # Wait 5 seconds for Discord to fully open

    # Click on the status dropdown
    pyautogui.click(x=104, y=1003)
    time.sleep(1)

    # Click on the "online" option
    pyautogui.click(x=110, y=879)
    time.sleep(1)

    # Type a new status message
    pyautogui.click(x=830, y=443)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    time.sleep(0.3)
    pyautogui.press('delete')
    time.sleep(0.2)
    pyautogui.click(x=830, y=443)
    pyautogui.typewrite(status)
    time.sleep(1)

    # Click on the "Save" button
    pyautogui.click(x=1113, y=707)
    time.sleep(1)

# Call the change_status function when the script is run
change_status()
