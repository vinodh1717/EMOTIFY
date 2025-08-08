# 🎵 EMOTIFY - Emotion-Based Music Player

EMOTIFY is an intelligent music player that uses facial emotion recognition to automatically play songs matching your current mood. Whether you're feeling happy, sad, angry, or neutral — EMOTIFY finds the perfect soundtrack for your emotions.

## 🚀 Features

- 🎭 Real-time emotion detection using webcam  
- 🧠 Facial expression recognition powered by deep learning  
- 🎶 Automatic mood-based music selection  
- 🗂️ Categorized music folders for each emotion  
- 🖥️ Simple and interactive GUI  

## 💡 How It Works

1. The system accesses your webcam and captures your facial expressions.  
2. A pre-trained model detects your emotion (Happy, Sad, Angry, Neutral, etc.).  
3. Based on your emotion, EMOTIFY selects and plays a song from the corresponding folder.  

## 🛠️ Tech Stack

- **Python 3.11**  
- **OpenCV** – For image capture and processing  
- **TensorFlow / Keras** – For emotion detection model  
- **Tkinter** – For the GUI  
- **Pygame / Playsound** – For audio playback  

## 📁 Folder Structure

```
emotify/
│
├── model/                  # Pre-trained emotion detection model
├── music/
│   ├── happy/
│   ├── sad/
│   ├── angry/
│   └── neutral/
├── main.py                 # Application entry point
├── detect_emotion.py       # Handles emotion prediction
├── gui.py                  # GUI logic
├── requirements.txt
└── README.md
```

## 🧪 Installation

```bash
# Clone the repository
git clone https://github.com/vinodh1717/EMOTIFY.git
cd EMOTIFY

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
python main.py
```

## 📷 Sample Screenshot

*(Add a screenshot here showing the GUI + webcam feed + detected emotion)*

## 📌 To-Do

- [ ] Add support for more emotions  
- [ ] Add Spotify API support  
- [ ] Improve UI/UX  
- [ ] Dockerize the app  

thank you
