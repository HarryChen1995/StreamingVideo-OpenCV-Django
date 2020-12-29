from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
# Create your views here.
import cv2
from django.views.decorators import gzip
def capframe():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame  = cap.read()
        ret, encodedframe = cv2.imencode(".jpeg", frame)
        encodedframe = encodedframe.tobytes()
        yield b'--frame\r\n'+b'Content-Type:image/jpeg\r\n\r\n' + encodedframe + b'\r\n'

def index(request):

    return render(request, "index.html")

@gzip.gzip_page
def feed(request):

    return StreamingHttpResponse(capframe(), content_type = "multipart/x-mixed-replace; boundary=frame")
