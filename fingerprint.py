import cv2
import numpy as np

def capture_fingerprint():
    # Simulate fingerprint scanning (Replace with actual fingerprint scanner SDK)
    print("Scanning fingerprint...")
    img = cv2.imread("fingerprint_sample.jpg", 0)  # Load fingerprint image
    return np.array(img).tobytes()  # Convert to byte array