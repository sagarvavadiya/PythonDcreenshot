# tasks/views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from PIL import ImageGrab
import pyautogui
import base64
import io

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def Screenshot(request):
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
    base64_screenshot = base64.b64encode(screenshot_bytes).decode()
    print("base64_screenshot",base64_screenshot)
    return HttpResponse(base64_screenshot)