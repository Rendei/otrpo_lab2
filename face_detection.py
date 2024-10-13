import cv2
import sys
import os

if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    image_path = os.path.join(os.path.dirname(__file__), 'photo.jpg')

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image '{image_path}' not found.")
    sys.exit(1)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Found {len(faces)} face(s)")

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
