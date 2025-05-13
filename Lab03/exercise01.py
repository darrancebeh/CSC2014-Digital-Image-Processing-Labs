import numpy as np;
import cv2

img = cv2.imread('Lab03/images/cameraman.bmp', 0)

height, width = img.shape[:2]

q_height = height // 2
q_width = width // 2

img[0:q_height, 0:q_width] = 0

cv2.imwrite('Lab03/solution_img/exercise01.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()