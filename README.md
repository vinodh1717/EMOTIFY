EMOTIFY
=======

Project Overview:
EMOTIFY is an Emotion-Based Music Player built using Python and OpenCV. It detects facial expressions and plays music that matches your mood.

Main Features:
- Real-time emotion detection using webcam.
- Music playback based on detected emotion.
- Built with Python, OpenCV, and TensorFlow.

Technologies Used:
- Python
- OpenCV
- TensorFlow/Keras
- Flask (if web interface is used)
- HTML/CSS (if applicable)
- Git & GitHub for version control

Setup Instructions:
1. Clone the repository:
   git clone https://github.com/vinodh1717/EMOTIFY.git
   cd EMOTIFY

2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Access the app (if web-based) at:
   http://127.0.0.1:5000/

Untracked / Unwanted Files:
- Virtual environment: venv/
- System files: .DS_Store, Thumbs.db
- Python cache: __pycache__/, *.pyc
- Environment variables: .env
- Large model files (optional): emotions_model.h5

Notes:
- Keep `.env` or sensitive information private.
- Virtual environment and cache files should not be pushed to GitHub.
- The application helps users play music based on detected emotions.
