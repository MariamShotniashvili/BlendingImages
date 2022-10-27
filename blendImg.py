import cv2
import numpy as np


def blend(img1, img2, w1, w2):
    img = np.zeros(shape=img1.shape, dtype="uint8")
    for i in range(img1.shape[1] - 1):
        for j in range(img1.shape[0] - 1):
            img[j][i] = w1 * img1[j][i] + w2 * img2[j][i]
    return img


if __name__ == '__main__':
    img1 = cv2.imread('img1.jpg')
    img2 = cv2.imread('img2.jpg')

    dsize = (img1.shape[1], img1.shape[0])

    # resize image
    new_img2 = cv2.resize(img2, dsize, interpolation=cv2.INTER_AREA)

    for i in range(0, 41, 2):
        img = blend(img1, new_img2, 0.1 + 0.01 * i, 0.9 - 0.01 * i)
        if i == 40:
            cv2.imshow("image", img)
            cv2.waitKey(0)
        else:
            cv2.imshow("image", img)
            cv2.waitKey(1)
