Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> img=cv2.imread('ganesh.png')
>>> cv2.imshow('image',img)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    cv2.imshow('image',img)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:973: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

>>> import cv2
>>> img=cv2.imread('ganesh.png')
>>> cv2.imshow('image',img)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cv2.imshow('image',img)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:973: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

