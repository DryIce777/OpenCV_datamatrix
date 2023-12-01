import numpy as np
import cv2
from pylibdmtx.pylibdmtx import decode

if __name__ == '__main__':

    image = cv2.imread('image.png', cv2.IMREAD_UNCHANGED);
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    msg = decode(thresh)
    print(msg)
