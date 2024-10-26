from PIL import Image

st.title("Image Test with Pillow")

if st.button("Upload Image"):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image')
