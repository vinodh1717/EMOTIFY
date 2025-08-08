
import cv2
import numpy as np
import pygame
import random
import os
from keras.models import load_model


# Load Pretrained Emotion Model

model = load_model('emotions_model.h5', compile=False)
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


# Initialize Music Player

pygame.init()
pygame.mixer.init()


# Load OpenCV Face Detector

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Play music based on emotion

def play_music(emotion):
    folder = f"music/{emotion.lower()}"
    if not os.path.exists(folder):
        print(f"[!] No folder for {emotion} emotion.")
        return
    songs = os.listdir(folder)
    if songs:
        song = random.choice(songs)
        path = os.path.join(folder, song)
        print(f"[🎵] Playing: {path}")
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    else:
        print(f"[!] No songs in {emotion} folder.")


# Start Webcam

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] Could not open webcam.")
    exit()

print("[INFO] Webcam initialized.")


# Main Loop

while True:

    # 1. Detect Emotion Once

    detected_emotion = None

    while detected_emotion is None:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            roi_resized = cv2.resize(roi, (64, 64)) / 255.0
            roi_reshaped = np.reshape(roi_resized, (1, 64, 64, 1))

            prediction = model.predict(roi_reshaped)
            detected_emotion = emotion_labels[np.argmax(prediction)]

            # Draw on frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, detected_emotion, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
            break

        cv2.imshow("Emotion DJ 🎧", frame)

        # Exit check
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            exit()

    print(f"[😃] Detected Emotion: {detected_emotion}")
    play_music(detected_emotion)


    # 2. Wait until music finishes

    while pygame.mixer.music.get_busy():
        cv2.imshow("Emotion DJ 🎧", frame)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            exit()

cap.release()
cv2.destroyAllWindows()
pygame.quit()