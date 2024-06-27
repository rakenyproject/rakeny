import cv2

def get_camera_frame():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        return None

    success, frame = cap.read()
    cap.release()

    if not success:
        return None

    return frame
