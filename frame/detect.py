import cv2
import os
import sys
from string import Template
count = 0
# first argument is the haarcascades path
face_cascade_path = '/usr/local/opencv/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml'
print(face_cascade_path)
face_cascade = cv2.CascadeClassifier(os.path.expanduser(face_cascade_path))

scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
flags = cv2.CASCADE_SCALE_IMAGE

for infname in sys.argv[1:]:
   image_path = os.path.expanduser(infname)
   image = cv2.imread(image_path)

   faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor, minNeighbors = min_neighbors,
    minSize = min_size, flags = flags)

   for( x, y, w, h ) in faces:
     count=count+1
     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
     outfname = "/tmp/%s.faces.jpg" % os.path.basename(infname)
     cv2.imwrite(os.path.expanduser(outfname), image)
print(count)
file = open("testfile.txt","w") 
file.write(str(count)) 
file.close() 
os.system("python sms.py")

