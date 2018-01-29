import cv2
import sys
import os
a=100
var=1
c=1000
vidcap = cv2.VideoCapture(os.path.expanduser(sys.argv[1]))
while var == 1:
	vidcap.set(cv2.CAP_PROP_POS_MSEC,a)      
	success,image = vidcap.read()

	if success:
		c=c+1
		a=a+300
		cv2.imwrite("frame/IMG_"+str(c)+".jpg", image)  
		os.system("python detect.py frame/IMG_"+str(c)+".jpg")  
    		#cv2.imshow("2sec",image)
    		#cv2.waitKey(0)  
	else:
		print "Done"
		break
os.system("python sms.py")
