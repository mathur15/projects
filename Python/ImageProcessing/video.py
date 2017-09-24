import cv2,time

video = cv2.VideoCapture(0)

check,frame = video.read()

while True:

	#loop over each frame quickly eventually forms a video

	check,frame = video.read()

	print(check)
	print(frame)

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	
	cv2.imshow("Capture",gray)

	key = cv2.waitKey(1)#keep making the current frame disappear so new one appears instantly 
	#show the video effect

	if key == ord('q'):
		break

video.release()
cv2.destroyAllWindows()