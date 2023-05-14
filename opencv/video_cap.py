import cv2
 
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./videos/1.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    # adjust width
    cap.set(3, 640)
    # adjust height
    cap.set(4, 480)
    # gray color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # show per frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
cap.release()
cv2.destroyAllWindows()
