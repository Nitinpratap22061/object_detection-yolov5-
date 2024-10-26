import streamlit as st
import cv2
import numpy as np

st.title("OpenCV Test")

# Test OpenCV version
st.write("OpenCV version:", cv2.__version__)

if st.button("Load Image"):
    # Create a dummy image (for testing)
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    cv2.circle(img, (100, 100), 50, (255, 0, 0), -1)  # Draw a blue circle
    st.image(img, channels="BGR", caption="Dummy Image")
