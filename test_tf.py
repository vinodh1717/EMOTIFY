# test_tf.py
import tensorflow as tf
print("✅ TensorFlow is working!")
print("TF version:", tf.__version__)
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
