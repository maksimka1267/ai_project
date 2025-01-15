import cv2
import numpy as np

img = cv2.imread('image/img.png')# загрузка фото

img =cv2.resize(img, (img.shape[1] // 2, img.shape[1] // 2)) # изменения размеров
img = cv2.GaussianBlur(img, (9, 9), 0) # размытие
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # отображение одного слоя цвета

img = cv2.Canny(img, 100, 100) #переведение в бинарный формат

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1) # увелечение обвотки

img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('test-image', img) # вывод картинки

# print(img.shape)

cv2.waitKey(0) # срок отображения
# cap = cv2.VideoCapture(0)# загрузка видео
# cap.set(3, 500)# изменения размеров
# cap.set(4, 500)# изменения размеров
#
# while True:
#     success, img =cap.read()
#     cv2.imshow('Result',img)# вывод видео
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break