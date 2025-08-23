EMOTIFY
==================

Project Overview:
EMOTIFY is an Emotion-Based Music Player. It detects facial expressions and plays music according to the detected mood. It helps users enjoy music that matches their current emotion.

Main Features:
- Real-time emotion detection using webcam
- Plays music based on detected emotion
- Built with Python, OpenCV, and TensorFlow

Technologies Used:
- Python
- OpenCV
- TensorFlow/Keras
- Flask (if web interface used)
- HTML/CSS (if applicable)

Setup Instructions:
1. Clone the repository:
   git clone https://github.com/vinodh1717/EMOTIFY.git
   cd EMOTIFY

2. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

Unwanted Files:
- venv/
- .DS_Store
- emotions_model.h5
- __pycache__/
- *.pyc
- .env
