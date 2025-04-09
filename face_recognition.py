import cv2
import face_recognition

def capture_face():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    cv2.destroyAllWindows()

    if not ret:
        return None
    return frame


def encode_face(image):
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings[0] if face_encodings else None


def match_face(stored_encoding, captured_image):
    captured_encoding = encode_face(captured_image)
    return face_recognition.compare_faces([stored_encoding], captured_encoding)[0]