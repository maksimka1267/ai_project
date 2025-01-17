import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl
from sympy import false
#открыли и поменяли цвет
img = cv2.imread('image/number_4.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#оптимизировали его для более быстрой работы и нашли края
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)
#нашли контуры
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
#отсортировали и выделили нужные контуры
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        pos=approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img=(cv2.bitwise_and(img, img, mask=mask))
x, y =np.where(mask == 255)
x1, y1 = np.min(x), np.min(y)
x2, y2= np.max(x), np.max(y)
crop = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text=text.readtext(crop)

res = text[0][-2]
print(res)
pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))

pl.show()
