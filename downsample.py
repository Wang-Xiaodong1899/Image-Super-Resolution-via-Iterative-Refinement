import cv2 as cv
import os

root = './valid/1k'
des = './valid/256px'
# img = cv.imread('1k/0001.png')
# low_img = cv.resize(img, None, fx=1/4, fy=1/4, interpolation=cv.INTER_CUBIC)
# cv.imwrite(os.path.join(des,'0001.png'),low_img)
if not os.path.exists(des):
    os.makedirs(des)

files = os.listdir(root)
cnt = 0
for file in files:
    suffix = os.path.splitext(file)[-1]
    if suffix == '.jpg' or suffix == '.png':
        cnt += 1
        print(cnt)
        img = cv.imread(os.path.join(root,file))
        low_img = cv.resize(img, None, fx=1/4, fy=1/4, interpolation=cv.INTER_CUBIC)
        cv.imwrite(os.path.join(des,file),low_img)