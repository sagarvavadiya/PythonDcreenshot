# tasks/views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from PIL import ImageGrab
import pyautogui
import pybase64
screen_width, screen_height = pyautogui.size()
screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
screenshot.save("screenshot.png")

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def Screenshot(request):
    screenshot.save("screenshot.png")
    print(screenshot)
    screenshot_bytes = screenshot.tobytes() 
    # Encode the bytes as a base64 string
    screenshot_base64 = pybase64.b64encode(screenshot_bytes).decode('utf-8') 
    print(screenshot_base64)
    return HttpResponse("Screenshot",screenshot_base64)