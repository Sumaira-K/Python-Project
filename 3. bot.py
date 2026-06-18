import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key= "YOUR_API_KEY"
)

time.sleep(2)  # small delay so you can switch to the target window



def is_last_message_from_sender():
    """
    Reads the latest copied message from clipboard
    and checks if it's from the sender.
    Returns True or False.
    """
    text = pyperclip.paste().strip().lower()

    if text.startswith("sender:"):
        return True
    return False

  

# Step 1: Click the chrome icon
pyautogui.click(1233, 1047)
time.sleep(0.5)




# Step 2: Drag to select the text
pyautogui.moveTo(685, 192)
pyautogui.dragTo(667, 1003, duration=0.7, button='left')

time.sleep(0.3)

# Step 3: Copy to clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1130, 576)
time.sleep(0.2)

# Step 4: Store in a variabl
chat_history = pyperclip.paste()

#print("Copied text:")
print(chat_history)




completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "YOUR_SYSTEM_PROMPT"},
        {"role": "user", "content": chat_history}
    ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)

# Step 1: Click at the new position
pyautogui.click(1042, 976)
time.sleep(0.2)

# Step 2: Paste the text
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.2)

# Step 3: Press Enter
pyautogui.press('enter')