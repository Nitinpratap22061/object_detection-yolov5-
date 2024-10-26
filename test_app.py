import streamlit as st
import cv2

st.title("OpenCV Test")

# Test OpenCV version
st.write("OpenCV version:", cv2.__version__)

if st.button("Test OpenCV"):
    img = cv2.imread('sample_image.jpg')  # Replace with a valid image path
    st.image(img, channels="BGR")
