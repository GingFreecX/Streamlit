import streamlit as st
import cv2
import numpy as np

st.title("🎥 Real-Time Video Stream with OpenCV")

# Sidebar controls
filter_type = st.sidebar.selectbox("Choose Filter", ["None", "Gray", "Canny Edge", "Blur"])
canny_low = st.sidebar.slider("Canny Threshold Low", 50, 150, 100)
canny_high = st.sidebar.slider("Canny Threshold High", 100, 300, 200)
blur_ksize = st.sidebar.slider("Blur Kernel Size", 1, 15, 3, step=2)

# Start webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened
if not cap.isOpened():
    st.error("Could not open webcam.")
else:
    snapshot_btn = st.button("📸 Take Snapshot")
    frame_placeholder = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        # Apply selected filter
        if filter_type == "Gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif filter_type == "Canny Edge":
            frame = cv2.Canny(frame, canny_low, canny_high)
        elif filter_type == "Blur":
            frame = cv2.GaussianBlur(frame, (blur_ksize, blur_ksize), 0)

        # Convert for Streamlit display
        if filter_type != "Gray" and filter_type != "Canny Edge":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif filter_type == "Gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        else:  # Canny
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

        frame_placeholder.image(frame, channels="RGB")

        # Snapshot functionality
        if snapshot_btn:
            cv2.imwrite("snapshot.jpg", frame)
            st.success("📸 Snapshot saved as snapshot.jpg")
            snapshot_btn = False
            break

    cap.release()
