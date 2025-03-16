'''import cv2
img=cv2.imread('ganesh.png')
gray=cv2.imread('ganesh.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('jai ganesha',img)
cv2.imshow('gray image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
#reading  videostream from camera
'''import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haar_cascade.xml")
while True:
  ret,frame=cap.read()
  if ret==False:
      continue
  faces=face_cascade.detectMultiScale(frame,1.3,5)
  for(x,y,w,h) in faces:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
  cv2.imshow('video frame',frame)
  key_pressed=cv2.waitKey(1) & 0xFF
  if key_pressed==ord('q'):
      break
cap.release()
cv2.destroyAllWindows()'''
#python script for capturing image from video stream and extracting faces 
#stores faces into numpy array
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haar_cascade.xml")
skip=0
face_data=[]
dataset_path='./data/'
filename=input("enter the name of the person:")
while True:
  ret,frame=cap.read()
  if ret==False:
      continue
  gray_frame=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(frame,1.3,5)
  faces=sorted(faces,key=lamda f:f[2]*f[3])
  #pick the last face(largest)
  for(x,y,w,h) in faces[-1:]:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
      #extact (crop out the required face)
      offset=10
      face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
      face_section=cv2.resize(face_section,(100,100))
      skip+=1
      if skip%10==0:
          face_data.append(face_section)
          print(len(face_data))
  cv2.imshow('video frame',frame)
  cv2.imshow('face section',face_section)
  #store every 10th face
  if(skip%10==0):
      #store the 10th face later on
      pass
  key_pressed=cv2.waitKey(1) & 0xFF
  if key_pressed==ord('q'):
      break
#convert our face list array into numpy array
face_data=np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)
#save this data into file system
np.save(dataset_path+filename+'.npy',face_data)

cap.release()
cv2.destroyAllWindows()