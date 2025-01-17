import cv2
import numpy as np

img = cv2.imread('image/people_5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#натренируем нашу модель
faces = cv2.CascadeClassifier('faces.xml')
#получим координаты лиц
#scaleFactor=2 значит что то что мы ищем может быть в 2 раза больше чем в тренировке
#minNeighbors=3 насколько много может быть найденых обьектов друг рядом с другом
results = faces.detectMultiScale(gray, scaleFactor=1.045, minNeighbors=5)

for (x, y, w, h) in results:
    square = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

cv2.imshow('Result', img)

cv2.waitKey(0)