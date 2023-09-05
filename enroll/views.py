# tasks/views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from PIL import ImageGrab
import pyautogui
import base64
import io
# Import datetime class from datetime module
from datetime import datetime

import pygetwindow as gw


import pygetwindow
import time
import os
import PIL
import ctypes
import pywin32

from screeninfo import get_monitors


# returns current date and time
now = datetime.now()


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def Screenshot2(request):
    # screen_width, screen_height = pyautogui.size()
    # screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)) 
    
    screenshot = ImageGrab.grab() 
    buffer = io.BytesIO() 
    screenshot.save("screenshot1.png")
    # print(screenshot)
    screenshot_bytes = screenshot.tobytes() 
    # base64_screenshot = base64.b64encode(buffer.getvalue()).decode()
    # Encode the bytes as a base64 string
    # screenshot_base64 = pybase64.b64encode(screenshot_bytes).decode('utf-8') 
    # base64_screenshot = base64.b64encode(screenshot_bytes).decode()
    # print("base64_screenshot",base64_screenshot)
    return HttpResponse("base64_screenshot")

def Screenshot3(request):
    # Get the active window
    active_window = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]

    # Get the coordinates of the active window
    left, top, right, bottom = active_window.left, active_window.top, active_window.right, active_window.bottom

    # Capture the active screen
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Convert the PIL Image to BytesIO
    image_buffer = io.BytesIO()
    screenshot.save("screenshot1.png")
    
    # Create a base64 encoded string of the image
    base64_image = base64.b64encode(image_buffer.getvalue()).decode()

    # Return the base64 encoded image as a JSON response
    return HttpResponse(base64_image, content_type="text/plain")

def Screenshot(request):
   
    def get_active_screen_id_windows():
        user32 = ctypes.windll.user32
        active_window = user32.GetForegroundWindow()
        active_screen_id = user32.MonitorFromWindow(active_window, 2)
        return active_screen_id

    active_screen_id = get_active_screen_id_windows()

    if active_screen_id:
        print(f"Active Screen ID: {active_screen_id}")
    else:
        print("No active screen found.")

 

    return HttpResponse(content_type="text/plain")