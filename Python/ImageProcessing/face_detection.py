import cv2

face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")#defines the features of the face to find

image = cv2.imread("Files/photo.jpg")#read the image

grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#instead of putting 0 in the read, we just get the grey version and read the 
#original in color

faces = face_cascade.detectMultiScale(grey_image,  #detect faces based on the cascade file
	scaleFactor=1.05,
	minNeighbors=5)
#reduces the image by 5% and finds again lower the number more the accuracy

for x,y,w,h in faces:
   img= cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)


cv2.imshow("SHOW", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
