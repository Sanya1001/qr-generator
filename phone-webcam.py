def phone_cam():
    import cv2
    import numpy as np

    url = 'http://192.168.1.4:8080/video'
    cap = cv2.VideoCapture(url)

    while True:
        camera, frame = cap.read()
        if frame is not None:
            cv2.imshow('Frame', frame)
        q = cv2.waitKey(1)
        if q & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()
