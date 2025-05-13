import cv2
import numpy as np

image_path1 = 'Lab03/images/dice1.png'
image_path2 = 'Lab03/images/dice2.png'

img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)

diff_image_color = cv2.absdiff(img1, img2)
diff_image_gray = cv2.cvtColor(diff_image_color, cv2.COLOR_BGR2GRAY)
_, thresh_binary_mask = cv2.threshold(diff_image_gray, 1, 255, cv2.THRESH_BINARY)

cv2.imshow("Difference Mask", thresh_binary_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()