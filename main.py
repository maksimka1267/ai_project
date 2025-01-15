import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# photo[100:150, 200:280] = 119, 201, 105

#отрисовка квадрата с зарисованной обвоткой
cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=3)

#отрисовка зарисованого квадрата
#cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=cv2.FILLED)

#отрисовка линии
cv2.line(photo, (0,photo.shape[0]//2), (photo.shape[1],photo.shape[0]//2), (119, 201, 105),thickness=3)

#отрисовка круга
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (119, 201, 105), thickness=1)

#отрисовка текста
cv2.putText(photo, 'Hello World!',(100, 150), cv2.FONT_HERSHEY_TRIPLEX,1, (255,0,0), thickness=2)
cv2.imshow('record', photo)
cv2.waitKey(0)