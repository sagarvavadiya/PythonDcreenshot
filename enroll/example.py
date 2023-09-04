import random
from PIL import ImageGrab
import pyautogui
import pybase64
screen_width, screen_height = pyautogui.size()
screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
# screenshot.save("screenshot.png")

def random_number():
    return random.randint(1, 10)

def Screenshot(request):
    screenshot.save("screenshot.png")
    print(screenshot)
    screenshot_bytes = screenshot.tobytes() 
    # Encode the bytes as a base64 string
    screenshot_base64 = pybase64.b64encode(screenshot_bytes).decode('utf-8') 
    print(screenshot_base64) 
