
import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import tempfile
import os

st.title("Fruit Detection")
model = YOLO('yolov8s.pt')

option = st.radio("Choose input type", ["Image", "Video", "Webcam"])

if option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        image.save("input.jpg")
        results = model("input.jpg")
        results[0].save(filename="output.jpg")
        st.image("output.jpg", caption="Detection Result")
elif option == "Video":
    video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    if video_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())
        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            annotated_frame = results[0].plot()
            stframe.image(annotated_frame, channels="BGR")
        cap.release()
elif option == "Webcam":
    st.info("Webcam support is only available when running locally.")
