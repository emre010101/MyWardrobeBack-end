import sys
from app.avatar.face_extractor import FaceExtractor
import cv2
import os

sys.path.insert(0, '..')

if __name__ == '__main__':
    extractor = FaceExtractor()
    input_image = '../assests/images/input/img.png'
    output_image = '../assests/images/output/normalised.png'

    print(f"Input image path: {os.path.abspath(input_image)}")
    print(f"Output image path: {os.path.abspath(output_image)}")

    face = extractor.extract_face(input_image)

    if face is not None:
        # Normalize the extracted face image
        normalized_face = extractor.normalize_face_image(face)

        # Save the normalized face image
        cv2.imwrite(output_image, normalized_face)
        print("Face extracted successfully.")
    else:
        print("No face detected.")
