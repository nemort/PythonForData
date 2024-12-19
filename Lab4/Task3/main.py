import cv2 as cv
from sys import argv

params = argv
vid_path = params[1]
cap = cv.VideoCapture(vid_path)
fps = cap.get(cv.CAP_PROP_FPS)
vid_name = vid_path.split("/")[-1]

if not cap.isOpened():
    print("Error: can't open file")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    text = f"Filename: {vid_name}, FPS:{fps} "
    cv.putText(frame, text, (10,30), cv.FONT_ITALIC, 1, (255, 255, 255), 2, cv.LINE_AA )
    cv.imshow(vid_name, frame)

    if cv.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
