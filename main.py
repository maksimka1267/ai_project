import cv2
import numpy as np

photo = cv2.imread('image/img.png')
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(),(200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (0, 300), (50,550), 255, -1)

img = cv2.bitwise_and(photo, photo, mask =square) #выводит только общие части
# img = cv2.bitwise_or(circle, square) #выводит полное обьединение
# img = cv2.bitwise_xor(circle, square) #выводит все, кроме общих частей
# img = cv2.bitwise_not(square) #инверсия

cv2.imshow('result', img)
cv2.waitKey(0)