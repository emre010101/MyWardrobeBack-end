import cv2
import cv2
import numpy as np

class FaceExtractor:
    def __init__(self):
        # Load the pre-trained Haar Cascade classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def extract_face(self, image_path, scale_factor=1.3, min_neighbors=5):
        # Read the image
        img = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)

        # Iterate through the detected faces and draw rectangles around them
        for (x, y, w, h) in faces:
            face = img[y:y+h, x:x+w]
            return face

        # If no face is detected, return None
        return None
    def normalize_face_image(face_image, target_size=(256, 256)):
        # Resize the face image to the target size
        resized_face = cv2.resize(face_image, target_size)

        # Convert the resized face image to grayscale
        gray = cv2.cvtColor(resized_face, cv2.COLOR_BGR2GRAY)

        # Create a mask for the face region (assuming a white background)
        _, mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

        # Dilate the mask to include more of the face
        kernel = np.ones((5, 5), np.uint8)
        dilated_mask = cv2.dilate(mask, kernel, iterations=1)

        # Apply the mask to remove the background
        face_with_transparent_bg = cv2.bitwise_and(resized_face, resized_face, mask=dilated_mask)

        return face_with_transparent_bg

    # Load the face image
    face_image = cv2.imread("path/to/face_image.png")

    # Normalize the face image
    normalized_face = normalize_face_image(face_image)

    # Save the normalized face image
    cv2.imwrite("path/to/normalized_face_image.png", normalized_face)