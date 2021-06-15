import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    i = 1
    range(1, 5, 1)
    for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(img, 'face,num'+str(i), (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                cv2.imshow('img', img)
                i = i + 1
                if i >= 5:
                    cv2.putText(img, 'PLEASE MAINTAIN SOCIAL DISTANCING!!!!!', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
