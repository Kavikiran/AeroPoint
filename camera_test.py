import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Can't open camera. Try index 1 or check permissions.")
else:
    print("Camera opened successfully. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Failed to read frame.")
            break
        cv2.imshow('camera test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
