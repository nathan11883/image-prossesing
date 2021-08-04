import cv2

rootfilepath= "data/"
file_name = rootfilepath + "yt1s.com - Motivational short video  How to succeed  cartoon.mp4"

cap = cv2.VideoCapture(file_name)
cap.set(3,640)
cap.set(4,480)

while True:
  success, img =cap.read()
  cv2.imshow("Video",img)
  if cv2.waitKey(1) & 0xFF ==ord("q"):
    break