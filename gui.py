import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from fingerprint import capture_fingerprint
from face_recognition import capture_face, encode_face, match_face
from database import insert_user


class BiometricApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fingerprint to Face Detection")
        self.root.geometry("600x400")

        # Style
        self.style = ttk.Style()
        self.style.theme_use('darkly')

        # Frame
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        # Labels
        ttk.Label(frame, text="Biometric Authentication", font=("Arial", 18)).pack(pady=10)

        # Buttons
        ttk.Button(frame, text="Register User", command=self.register_user, bootstyle="success").pack(pady=5)
        ttk.Button(frame, text="Authenticate", command=self.authenticate_user, bootstyle="primary").pack(pady=5)

    def register_user(self):
        name = "Test User"  # Replace with user input
        fingerprint = capture_fingerprint()
        face_img = capture_face()
        face_encoding = encode_face(face_img)

        if fingerprint and face_encoding is not None:
            insert_user(name, fingerprint, face_encoding)
            messagebox.showinfo("Success", "User Registered Successfully!")
        else:
            messagebox.showerror("Error", "Face or Fingerprint not detected.")

    def authenticate_user(self):
        # Simulate authentication process
        stored_fingerprint = capture_fingerprint()  # Retrieve from DB in real use
        captured_face = capture_face()

        if match_face(stored_fingerprint, captured_face):
            messagebox.showinfo("Access Granted", "Authentication Successful!")
        else:
            messagebox.showerror("Access Denied", "Face or Fingerprint did not match.")


if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = BiometricApp(root)
    root.mainloop()