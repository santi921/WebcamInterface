# Example for how to use the opencv module to campure webcam images

# Import opencv
import cv2
import numpy as np
import ShapeDetector as sd
import CameraOps as co


# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key
def stream(n=0):
	cv2.namedWindow("preview")
	vc = cv2.VideoCapture(n)

	if vc.isOpened(): # try to get the first frame
	    rval, frame = vc.read()
	    print('frame\n', frame[0][:])
	else:
	    rval = False
	    frame = None

	while rval:
	    cv2.imshow("preview", frame)
	    rval, frame = vc.read()
	    key = cv2.waitKey(20)
	    if key == 27: # exit on ESC
	        break

	cv2.destroyWindow("preview")
	vc.release()
	
# Function taking a single picture from webcam and returning it in array form
# n: Camera number on computer (usually n=0 for built-in webcam)
def snap(n=0):
	cv2.namedWindow("preview")
	vc = cv2.VideoCapture(n)

	if vc.isOpened(): # try to get the first frame
	    rval, frame = vc.read()
	    print('frame\n', frame[0][:])
	else:
	    rval = False
	    frame = None

	cv2.destroyWindow("preview")
	vc.release()
	#frame=np.array(frame)
	#print('size', np.shape(frame))
	return frame


if __name__=='__main__':

	#Uncomment to stream webcam video
	#stream()

	# #Uncomment to take single snap
	##print(s)










	#Uncomment to take single snap
	#add n in the future to distinguish images from one another, this might be a time 
	s = co.snap(0)
	count=0
	
	r=[]
	b=[]
	g=[]
	#parse image to use in thresholding
	cv2.imwrite("frame%d.jpg" % count, s) 
	img = cv2.imread("frame%d.jpg" % count)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
	contrs=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	
	for i in range(s.shape[0]):
		for j in range(s.shape[1]):
			#x
			#y
			#color
			r.append(s[i][j][0])
			b.append(s[i][j][1])
			g.append(s[i][j][2])
			

	r=np.array(r)
	b=np.array(b)
	g=np.array(g)
	mean=[np.mean(r),np.mean(b),np.mean(g)]
	var=[np.var(r),np.var(b),np.var(g)]
	#print(mean)
	#print(var)
	print(np.shape(contrs[0]))
	print(np.shape(contrs[1]))
	
	for i in contrs[1]:
		sides=sd.detect(contrs[1])
		if sides=="Rect":
			breaker=contrs[1]
	


	#print(sides)

