import argparse
import cv2
import sys

parser = argparse.ArgumentParser(description="Face detection on an image.")
parser.add_argument('image_path', nargs='?', default='photo_1.jpg', help='Path to the image file')

args = parser.parse_args()
image_path = args.image_path

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image from {image_path}")
    sys.exit(1)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Found {len(faces)} face(s)")

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

output_image_path = f"{image_path.split(".jpg")[0]}_output.jpg"
cv2.imwrite(output_image_path, image)
print(f"Saved output image to {output_image_path}")

cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
