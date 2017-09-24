import cv2
import glob

images = glob.glob("sample-images/*.jpg")

for image in images:
	img = cv2.imread(image,0)
	resized = cv2.resize(img,(100,100))
	cv2.imshow(image,resized)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	cv2.imwrite("resized_"+image,resized)
