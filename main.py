import cv2
import numpy as np

# photo = np.zeros((450, 450, 3), dtype='uint8')
#
# # photo[100:150, 200:280] = 119, 201, 105
#
# #отрисовка квадрата с зарисованной обвоткой
# cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=3)
#
# #отрисовка зарисованого квадрата
# #cv2.rectangle(photo, (0, 0), (100, 100), (119, 201, 105), thickness=cv2.FILLED)
#
# #отрисовка линии
# cv2.line(photo, (0,photo.shape[0]//2), (photo.shape[1],photo.shape[0]//2), (119, 201, 105),thickness=3)
#
# #отрисовка круга
# cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (119, 201, 105), thickness=1)
#
# #отрисовка текста
# cv2.putText(photo, 'Hello World!',(100, 150), cv2.FONT_HERSHEY_TRIPLEX,1, (255,0,0), thickness=2)
# cv2.imshow('record', photo)
# cv2.waitKey(0)


# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     img = cv2.GaussianBlur(img, (9,9), 0)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     img = cv2.Canny(img, 50, 50)
#
#     kernel = np.ones((5,5),np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#
#     img =cv2.erode(img, kernel, iterations=1)
#
#
#     cv2.imshow('result', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
img =cv2.imread('image/img.png')
new_img = np.zeros(img.shape, dtype='uint8')
#перевернуть
# img = cv2.flip(img, -1)
# вращение картинки
def rotate(img_param, angle):
        height, width = img_param.shape[:2]
        point = (width // 2, height // 2)

        mat = cv2.getRotationMatrix2D(point, angle, 1)
        return cv2.warpAffine(img, mat, (height, width))

# img = rotate(img, -90)
# отступ картинки
def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, mat, (img_param.shape[1], img_param.shape[0]), 1)

# img = transform(img, 30, 200)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)


img = cv2.Canny(img, 100, 100)
#контуры изображения
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#отрисовка по контурам
cv2.drawContours(new_img, con, -1, (233, 111, 148), 1)

cv2.imshow('result',new_img)

cv2.waitKey(0)