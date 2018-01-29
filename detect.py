import cv2
import os
import sys
from string import Template
count = 0
# first argument is the haarcascades path
#please edit below path
path = 'Path to haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(os.path.expanduser(path))

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
     outfname = "detected/%s.faces.jpg" % os.path.basename(infname)
     cv2.imwrite(os.path.expanduser(outfname), image)
file = open("testfile.txt","r") 
xcount=file.read()
num=int(xcount)
file.close()
if(count>num):
	file = open("testfile.txt","w") 
	file.write(str(count)) 
	file.close() 
#file = open("testfile.txt","w") 
#file.write(str(count)) 
#file.close() 


