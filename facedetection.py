import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
img = cv2.imread('VDS.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
i = 1
range(1,5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img, 'face,num'+str(i), (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 0), 2)
    cv2.imshow('img', img)
    i = i+1
    if i > 5:
        cv2.putText(img, 'PLEASE MAINTAIN SOCIAL DISTANCING!!!!!', (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
cv2.waitKey(None)